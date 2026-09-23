"""Arithmetic and document checks, not a verifier of live travel facts."""
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
from content import DAYS, REQUIRED, SOURCES

ROOT = Path(__file__).resolve().parent
errors = []
def check(test, message):
    if not test: errors.append(message)
def minutes(t):
    h,m = map(int,t.split(':'))
    return h*60+m
def show(n): return f'{n//60:02}:{n%60:02}'

coverage=set()
for day in DAYS:
    check(datetime.fromisoformat(day['date']).strftime('%a') == day['label'][:3], f'{day["id"]}: weekday mismatch')
    rows=day['rows']
    for r in rows:
        check(bool(r['kind']) and bool(r['mode']), f'Missing type/mode: {r["name"]}')
        check(0 <= r['low'] <= r['high'], f'Invalid transfer: {r["name"]}')
        check(r['source'] is None or r['source'] in SOURCES, f'Unknown source: {r["name"]}')
        coverage.update(r['cover'])
    if day['id'] in ('d1','d7'): continue  # Flights have local time-zone changes.
    check(minutes(rows[0]['time']) >= 600, f'{day["id"]}: starts before 10:00')
    previous_end=None
    for r in rows:
        start=minutes(r['time'])
        if previous_end is not None:
            check(start >= previous_end, f'{day["id"]}: {r["name"]} departs {show(start)} before prior finish {show(previous_end)}')
        arrival=start+r['high']
        visit_start=arrival
        if r['slot']:
            target=minutes(r['slot'])
            check(arrival <= target-r['buffer'], f'{day["id"]}: {r["name"]} misses its stated buffer')
            visit_start=max(arrival,target)
        if r['opening']:
            check(visit_start >= minutes(r['opening']),f'{r["name"]}: before opening')
        previous_end=visit_start+r['visit']
        if r['close']:
            check(previous_end <= minutes(r['close']),f'{r["name"]}: ends after closing')
    check(previous_end >= 18*60+30,f'{day["id"]}: ends before 18:30')
    print(f'{day["label"]}: {rows[0]["time"]} to {show(previous_end)}, upper transfer estimates, no dinner counted')

check(REQUIRED <= coverage, 'Missing sights: '+', '.join(sorted(REQUIRED-coverage)))
airport=DAYS[-1]['rows'][2]
check(minutes(airport['time'])+airport['high'] <= minutes(airport['slot'])-airport['buffer'], 'Airport margin violated')
check(minutes(airport['slot'])-(minutes(airport['time'])+airport['high']) >= 165,'Less than 2¾ hours at airport')
check(minutes('21:35')-minutes('18:25')+60 == 250, 'Outbound elapsed flight time')
check(minutes('17:35')-minutes('12:45')-60 == 230, 'Inbound elapsed flight time')
check(len(DAYS)==7 and DAYS[0]['date']=='2026-12-18' and DAYS[-1]['date']=='2026-12-24','Date range')

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.anchors=[]; self.tags=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag=='a' and attrs.get('href','').startswith('#'): self.anchors.append(attrs['href'][1:])
        if tag not in ('meta','link','br','hr','img','input','source','wbr','area','base','embed','param','track','col'):
            self.tags.append(tag)
    def handle_endtag(self,tag):
        check(bool(self.tags) and self.tags[-1]==tag,f'Unbalanced HTML closing tag {tag}')
        if self.tags: self.tags.pop()

html=(ROOT/'index.html').read_text()
doc=Document(); doc.feed(html)
check(not doc.tags, 'Unclosed HTML tags')
check(len(doc.ids)==len(set(doc.ids)), 'Duplicate HTML IDs')
check(set(doc.anchors)<=set(doc.ids), 'Broken internal navigation')
for name in ('content.py','index.html','itinerary.md'):
    check('\u2014' not in (ROOT/name).read_text(),f'Em dash in {name}')
check('Waldstein' in html and 'Closed in December' in html, 'Seasonal omission not explained')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
print('PASS: 0 arithmetic or structural issues. Live access, route estimates and unpublished slots still require manual checks.')

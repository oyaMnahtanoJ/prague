"""Route coverage and document checks; no visit timetable is maintained."""
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
import re
from content import DAYS, REQUIRED, SOURCES

ROOT = Path(__file__).resolve().parent
errors = []
def check(test, message):
    if not test: errors.append(message)
coverage=set()
for day in DAYS:
    check(datetime.fromisoformat(day['date']).strftime('%a') == day['label'][:3], f'{day["id"]}: weekday mismatch')
    rows=day['rows']
    for r in rows:
        check(bool(r['kind']) and bool(r['mode']), f'Missing type/mode: {r["name"]}')
        check(0 <= r['low'] <= r['high'], f'Invalid transfer: {r["name"]}')
        check(not {'time','visit','slot'} & r.keys(), f'Timetable field remains: {r["name"]}')
        coverage.update(r['cover'])
    if day['id'] not in ('d1','d7'):
        check(not re.search(r'\b\d{1,2}:\d{2}\b',str(day)),f'{day["id"]}: sightseeing clock time remains')
    print(f'{day["label"]}: {len(rows)} ordered stops; transfer times only')

check(REQUIRED <= coverage, 'Missing sights: '+', '.join(sorted(REQUIRED-coverage)))
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
check('<h1>Prague</h1>' in html and '<title>Prague</title>' in html,'Incorrect headline')
for unwanted in ('id="sources"','class="stats"','class="time"','class="duration"','Planning edition','Residence Agnes','Hotel Josef','Hotel Haštal','Charles University','Náměstí Míru','Náměstí Republiky Christmas Market','15:15','18:00'):
    check(unwanted not in html, f'Removed content remains: {unwanted}')
check(sum(r['kind']=='Christmas market' for d in DAYS for r in d['rows'])==2,'Must have two market stops')
check('three hours before departure' in html,'Missing airport margin guidance')
from build import price
check(price(100)=='CZK 100 (≈NIS 14)','CZK conversion regression')
check(price(686,'USD')=='USD 686 (≈NIS 2,070)','USD conversion regression')
check(price(450,upper=800)=='CZK 450–800 (≈NIS 64–113)','Range conversion regression')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
print('PASS: route coverage, requested removals, transfers, conversions and HTML structure. Live access and routes require manual checks; no timetable is claimed.')

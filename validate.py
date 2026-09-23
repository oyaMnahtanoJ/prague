"""Route coverage and document checks; no visit timetable is maintained."""
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
import re
from content import DAYS, REQUIRED, SOURCES, BASE, HOTEL, BOOKINGS

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
check(re.findall(r'class="daynum"[^>]*>(\d+)</div>',html)==['0','1','2','3','4','5'], 'Expected Day 0 and sightseeing days 1–5 only')
departure=html.split('<article class="day" id="d7">',1)[1].split('</article>',1)[0]
check('class="daynum"' not in departure and '<h2>Departure</h2>' in departure, 'Departure must be unnumbered')
check('Day 7' not in html and 'Day 7' not in (ROOT/'itinerary.md').read_text(), 'Stale departure day number')
for unwanted in ('id="sources"','class="stats"','class="time"','class="duration"','Planning edition','Residence Agnes','Hotel Josef','Hotel Haštal','Charles University','Náměstí Míru','Náměstí Republiky Christmas Market','15:15','18:00','Kafka','Kampa','Na Kampě','Crystal Garden'):
    check(unwanted not in html, f'Removed content remains: {unwanted}')
check(sum(r['kind']=='Christmas market' for d in DAYS for r in d['rows'])==2,'Must have two market stops')
check('three hours before departure' in html,'Missing airport margin guidance')
check('no more than half the day' in html,'Missing Troja half-day limit')
check('hall' in {c for r in DAYS[2]['rows'] for c in r['cover']}, 'Old Town Hall not moved to Sunday')
check('Jungmann Hotel' in BASE and 'Jungmannovo náměstí 2' in BASE, 'Wrong hotel routing base')
check(DAYS[0]['rows'][0]['target']==BASE, 'Arrival map does not point to booked hotel')
check(all('Bolt' in DAYS[i]['rows'][0]['mode'] for i in (0,6)), 'Airport legs must use Bolt')
check('TLV 18:25 → PRG 21:35' in DAYS[0]['intro'], 'Outbound ticket times changed')
check('PRG 12:45 → TLV 17:35' in DAYS[6]['intro'], 'Return ticket times changed')
check(all('Confirmed ticket times' in DAYS[i]['intro'] for i in (0,6)), 'Flight confirmation missing')
check(not any(t=='Flights and hotel' for _,t,_,_ in BOOKINGS), 'Booked hotel remains on must-book list')
for name in ('index.html','itinerary.md','README.md'):
    document=(ROOT/name).read_text()
    for stale in ('Haštalsk','Dlouhá třída','hotel area','Supplied fare','choose the hotel','Where to stay','Provisional','provisional'):
        check(stale not in document, f'Stale hotel or flight wording in {name}: {stale}')
check(DAYS[3]['rows'][0]['high']<=5, 'Shopping route still uses old hotel transfer')
check('2–5 min' in DAYS[5]['dinner'], 'Market return not updated for Jungmann Hotel')
from build import price
check(price(100)=='CZK 100 (≈NIS 14)','CZK conversion regression')
check(price(686,'USD')=='USD 686 (≈NIS 2,070)','USD conversion regression')
check(price(450,upper=800)=='CZK 450–800 (≈NIS 64–113)','Range conversion regression')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); raise SystemExit(1)
print('PASS: route coverage, requested removals, transfers, conversions and HTML structure. Live access and routes require manual checks; no timetable is claimed.')

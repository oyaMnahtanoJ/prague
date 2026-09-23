"""Render the single-file website and its plain Markdown companion."""
from pathlib import Path
from html import escape as e
from urllib.parse import urlencode
from content import DAYS, HOTELS, BOOKINGS, MARKETS, SOURCES, UPDATED

ROOT = Path(__file__).resolve().parent

def duration(n):
    if n >= 60 and n % 15 == 0:
        whole, rem = divmod(n, 60)
        return f'{whole}{ {0:"",15:"¼",30:"½",45:"¾"}[rem]} h'
    return f'{n} min'

def transfer(r):
    if r['high'] == 0:
        return f"{r['mode']} · included in block"
    span = str(r['low']) if r['low'] == r['high'] else f"{r['low']}–{r['high']}"
    return f"{r['mode']} · {span} min"

def source(key, label='Official information'):
    if not key:
        return ''
    title, url = SOURCES[key]
    return f'<a href="{e(url, quote=True)}" title="{e(title, quote=True)}">{e(label)}</a>'

def maplink(r):
    return 'https://www.google.com/maps/search/?' + urlencode({'api':1,'query':r['target']})

def block(title, prose):
    return f'<div class="info"><b>{e(title)}.</b> {e(prose)}</div>'

def day_html(day, number):
    rows = []
    for r in day['rows']:
        dur = f' · visit {duration(r["visit"])}' if r['visit'] else ''
        slot = ''
        if r['slot'] and r['kind'] != 'airport':
            slot = f'<p class="note"><b>Unconfirmed target: {r["slot"]}; be there {r["buffer"]} min early.</b></p>'
        rows.append(f'''<li><div class="time">{e(r['time'])}</div><div>
        <span class="place">{e(r['name'])}</span> <span class="type">({e(r['kind'])})</span><br>
        <span class="transfer">{e(transfer(r))}</span><span class="duration">{e(dur)}</span>
        <p class="detail">{e(r['text'])}</p>{slot}
        {f'<p class="note">{e(r["note"])}</p>' if r['note'] else ''}
        <div class="links"><a href="{e(maplink(r), quote=True)}">Map pin</a>{source(r['source'])}</div></div></li>''')
    notes = ''.join(block(t,p) for t,p in day['notes'])
    dinner = f'<p class="dinner">{e(day["dinner"])}</p>' if day['dinner'] else ''
    return f'''<article class="day" id="{day['id']}"><header class="day-head"><div class="daynum">{number}</div>
    <div><div class="date">{e(day['label'])}</div><h2>{e(day['title'])}</h2><div class="pill">{e(day['load'])}</div></div></header>
    <p class="intro">{e(day['intro'])}</p><ol class="schedule">{''.join(rows)}</ol><div class="day-bottom">{dinner}{notes}</div></article>'''

TRANSPORT = [
 ('Walking first', 'Walk short central hops, normally up to about 22 minutes, with slower uphill allowances. A map pin identifies the destination, not a verified walking route. The final hotel address can alter the first and last legs.'),
 ('Public transport for two', 'Trams and metro are the default for longer city hops. Both travellers need their own valid ticket. Transfers are included within the ticket’s validity; allow for activation before boarding and follow the app’s countdown. Validate paper tickets once at the start, not on every change.'),
 ('Selective cars', 'Use Bolt or Uber for the two airport legs and the Sunday cross-city garden transfer. Compare the total fare for one car with two transit tickets, including walking and waiting. Surge pricing can erase any advantage. Lyft is not a Prague ride-hailing option in this plan.'),
 ('Which tickets to buy', 'Use singles on walking-heavy days. A 24-hour ticket on Wednesday is particularly useful because it includes both Petřín funicular rides. Do not automatically buy five full days of passes: one 72-hour plus two 24-hour app tickets costs CZK 620 per adult, CZK 1,240 for two, and may exceed what you actually use.'),
 ('Airport alternative', 'For lower cost, the ordinary trolleybus 59 plus metro A and a final walk is usually about 60–80 minutes door to door from this base, with a 90-minute Prague ticket. That is CZK 92 for two in the app, excluding any luggage supplements that apply. It is not the Airport Express. With a late arrival and a Christmas Eve departure, the planned car transfers buy useful convenience.'),
]
FARES = [('30 minutes','36','72','39'),('90 minutes','46','92','50'),('24 hours','140','280','150'),('72 hours','340','680','350')]
PENDING = [
 'Choose the exact hotel, then recalculate hotel-to-first-stop and last-stop-to-hotel legs. No accommodation or transport is booked by this page.',
 'Confirm the Municipal House English tour on 22 December first, then the Old Town Hall English tour. The proposed 18:00 and 15:15 are planning targets, not published December slots.',
 'Confirm 2026 Christmas exceptions, cathedral services, seasonal garden entrances and current tram/bus routing shortly before departure. Normal winter hours are not a promise that no special closure will occur.',
 'If interested in Crystal Garden, verify the 20 December evening programme, entry product and cancellation conditions. It replaces the Sunday market evening; it is not an extra stop squeezed into the same time.',
 'Confirm the Náměstí Republiky market’s evening closing time; if needed, see its stalls before the Municipal House tour.',
 'Check the forecast and functioning of the Petřín funicular before committing to tower tickets. Keep the Strahov substitute as an alternative, not another compulsory stop.',
 'Confirm Christmas Eve breakfast, the 09:15 airport pickup and the airline’s latest reporting instructions. Pack on Wednesday evening.',
]

def build():
    nav = ''.join(f'<a href="#{d["id"]}">{e(d["label"])}</a>' for d in DAYS)
    overview = ''.join(f'<a href="#{d["id"]}">{e(d["label"].split(" · ")[0])} {d["date"][-2:]}</a><span>{e(d["title"])}</span>' for d in DAYS)
    hotels = ''.join(f'<div class="panel"><h3>{e(t)}</h3><p>{e(p)}</p><p class="small">{e(n)}</p></div>' for t,p,n in HOTELS)
    bookings = ''.join(f'<div class="booking"><span class="when">{e(w)}</span><h3>{e(t)}</h3><p>{e(p)}</p>{source(s)}</div>' for w,t,p,s in BOOKINGS)
    markets = ''.join(f'<div class="panel"><h3>{e(n)}</h3><p>{e(why)}</p><p class="small">{e(dates)}<br>{e(day)}</p>{source(s)}</div>' for n,why,dates,day,s in MARKETS)
    fares = ''.join('<tr>'+''.join(f'<td>{e(cell)}</td>' for cell in cells)+'</tr>' for cells in FARES)
    transports = ''.join(f'<h3>{e(t)}</h3><p>{e(p)}</p>' for t,p in TRANSPORT)
    pending = ''.join(f'<li>{e(p)}</li>' for p in PENDING)
    sources = ''.join(f'<li><a href="{e(url, quote=True)}">{e(title)}</a></li>' for title,url in SOURCES.values())
    html = f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="A sleep-first Prague Christmas itinerary for two: 18–24 December 2026, five full days, botanical gardens, markets and a full shopping day.">
<title>Prague at Christmas · 18–24 December 2026</title><style>{(ROOT/'style.css').read_text()}</style></head><body>
<a href="#itinerary" class="skip">Skip to itinerary</a>
<header class="masthead container"><div class="eyebrow">A Christmas week for two · 18–24 December 2026</div>
<h1>Prague, at your own pace.</h1><p class="lede">Slow breakfasts, full days. Castle courtyards, tropical greenhouses, bookshops and Christmas lights, with the city arranged one neighbourhood at a time.</p>
<div class="stats"><div class="stat"><b>5 full days</b><span>6 nights · 2 travellers</span></div><div class="stat"><b>10:00 starts</b><span>Every sightseeing day</span></div><div class="stat"><b>2 gardens</b><span>Plus 4 selected markets</span></div><div class="stat"><b>1 shopping day</b><span>Monday kept free</span></div></div>
<div class="actions"><a href="itinerary.md">Plain-text itinerary</a><a href="https://github.com/oyaMnahtanoJ/prague">GitHub source</a><button type="button" onclick="window.print()">Print / save PDF</button></div>
<p class="small">Planning edition · reviewed {UPDATED} · flights assumed, hotel not selected, no bookings made.</p></header>
<nav class="jump" aria-label="Jump to day or planning section"><div class="container">{nav}<a href="#stay">Stay</a><a href="#transport">Transport</a><a href="#book">Book</a><a href="#sources">Sources</a></div></nav>
<main class="container" id="itinerary"><section aria-labelledby="week"><h2 id="week">The week at a glance</h2><div class="panel overview">{overview}</div>
{block('Flights being used','Smartwings, as supplied: Fri 18 Dec, TLV 18:25 → PRG 21:35; Thu 24 Dec, PRG 12:45 → TLV 17:35. All times local. Quoted US$686 for two, not re-priced or booked.')}
{block('How to read the times','The left-hand time means leave the previous stop, then allow the stated transfer and visit. Transfer ranges are planning estimates including ordinary waits where indicated, not routing-engine measurements. The upper end fits the following row; unexpected queues require shortening a flexible block. Airport-arrival rows are approximate, and flight times use their stated local time zones.')}
<p class="small">The route assumes a hotel near Haštalské náměstí. All five sightseeing days start at 10:00 and have activities until approximately 19:00–19:45, before dinner. The airport transfer on 24 December is the necessary exception. Outdoor sights are prioritised in the limited winter daylight; most evening time is indoors or among the market lights.</p></section>
{''.join(day_html(d,i) for i,d in enumerate(DAYS,1))}
<section id="stay"><h2>Where to stay</h2><p class="lede">My first choice: a quiet room near Haštalská, not directly above Dlouhá’s nightlife.</p>{hotels}
<div class="panel"><h3>Three properties to compare</h3><p>{source('agnes','Residence Agnes')} on Haštalská; {source('josef','Hotel Josef')} on Rybná; {source('hastal','Hotel Haštal')} by Haštalské náměstí. These are location-based shortlist suggestions, not checked offers or promises of a quiet room.</p><p class="small">Compare the full six-night price for two with breakfast, refundable terms and late check-in. Ask for a rear-facing room away from lifts and street noise. At Residence Agnes, check the room’s stair access if booking an upper or attic category. Rates and December availability have not been checked.</p></div></section>
<section id="gardens"><h2>Which botanical gardens?</h2><div class="panel"><p><b>Two principal public botanical gardens are worth considering for this trip:</b> Prague Botanical Garden in Troja, including its Fata Morgana tropical greenhouse, and Charles University’s smaller garden on Na Slupi. Both are included on Sunday. Fata Morgana is part of Troja, not a third garden.</p><p>There are other specialised or educational plant collections, so this is not a claim that Prague contains exactly two botanical institutions. For your five-day visit, these two provide the useful shortlist. Formal gardens such as Waldstein are a different category, and Waldstein is closed in December.</p><p class="small">{source('troja','Troja winter hours')} · {source('university','University garden hours')} · {source('waldstein','Waldstein seasonal access')}</p></div></section>
<section id="markets"><h2>The Christmas markets</h2><p class="lede">Four worthwhile markets, not four identical evenings. Old Town Square and Wenceslas Square are the flagships; Míru adds a neighbourhood setting; Republiky fits naturally beside the Municipal House.</p><div class="grid">{markets}</div><p class="small">Prague has more seasonal markets and pop-ups; there is no single permanent citywide count. Four is the selected route, not the total number. Dates above are the published 2026 listings; recheck individual stall hours and any changes before travel. Market browsing is intentionally distinct from the daytime shopping day.</p></section>
<section id="transport"><h2>Getting around, and what it costs</h2><p class="lede">For two people, public transport usually wins on price. Use cars where the luggage or time saved makes the extra cost worthwhile.</p><div class="panel">{transports}<p class="small">{source('fares','Official PID fares')} · {source('pid','Check the actual route')} · {source('funicular','Funicular rules')}</p></div>
<div class="panel"><h3>2026 Prague fares, CZK</h3><div class="table-scroll"><table><thead><tr><th scope="col">Validity</th><th scope="col">App / adult</th><th scope="col">App / two adults</th><th scope="col">Paper / adult</th></tr></thead><tbody>{fares}</tbody></table></div><p class="small">Prices are per ticket, not per vehicle. Petřín is included in 24-hour and 72-hour tickets, but not ordinary 30-minute or 90-minute tickets. A standalone funicular ride is CZK 90 in the app or CZK 100 otherwise, per person, one way.</p>
<h3>Car budgeting, per vehicle for both of you</h3><p>Allow roughly <b>CZK 120–250 for a short central hop</b>, <b>CZK 200–400 for a longer cross-city trip</b> and <b>CZK 450–800 each way to the airport</b>. These are budgeting estimates, not live quotes, fixed prices or caps; a busy period can cost more. Confirm the app’s total before ordering.</p><p>For comparison, two 30-minute app tickets total CZK 72, and two 90-minute tickets CZK 92. A car at CZK 200 therefore costs CZK 108–128 extra for that journey, not twice the quoted car price.</p><p class="small">{source('bolt','Bolt’s published example estimate')} is a reference point, not a quote for your travel dates. No car hire is needed. Keep costs in CZK to avoid pretending an exchange rate will remain fixed.</p></div></section>
<section id="book"><h2>What to book, and when</h2><p class="lede">Protect cancellation flexibility. Book the room on refundable terms; commit to experiences once the trip is secure and suitable slots are released.</p><div class="panel">{bookings}</div></section>
<section id="checks"><h2>Before this becomes the final plan</h2><div class="panel"><ul class="checklist">{pending}</ul></div>
{block('What is checked','The build checks timetable overlaps using the upper transfer estimate, stated pre-tour buffers, listed closing times, coverage of the requested sights, sightseeing start and finish times, and the airport deadline. Those arithmetic checks do not verify road access, live queues, the final hotel route, future opening hours or ticket availability. These remain source-based and manual checks.')}
<p class="small">No river cruise, sightseeing-only cable-car ride or modern-art gallery has been added. The funicular has a transport purpose: reaching Petřín without a long climb. Sightseeing starts at 10:00; the earlier departure-day breakfast and transfer are the only exception.</p></section>
<section id="sources"><h2>Sources and live checks</h2><p class="small">Official operator and destination sources reviewed for this planning edition. Linked pages can change. December-specific programmes take precedence over regular winter hours; map links are destination searches, not claimed verification of travel times.</p><ul class="sources">{sources}</ul></section></main>
<footer class="footer"><div class="container">Prague · 18–24 December 2026 · two travellers<br>Editable source: content.py · regenerate: python3 build.py · check: python3 validate.py<br>Public planning document. No reservation references, credentials or private contact details.</div></footer></body></html>'''
    (ROOT/'index.html').write_text(html, encoding='utf-8')

    md = ['# Prague at Christmas: 18–24 December 2026', '', f'Reviewed {UPDATED}. Two travellers; six nights; five full days. Flights assumed, not booked. Hotel base provisionally Haštalské náměstí.', '', 'Every sightseeing day starts at 10:00. Each time below is departure from the previous stop, followed by its transfer and visit. Transfer times are estimates, not measured routes. The final hotel and December English tours remain to be confirmed.', '']
    for day in DAYS:
        md += [f'## {day["label"]}: {day["title"]}', '', day['intro'], '']
        for r in day['rows']:
            md += [f'- **{r["time"]}** {r["name"]} ({r["kind"]}); {transfer(r)}' + (f'; visit {duration(r["visit"])}.' if r['visit'] else '.'), f'  {r["text"]}']
            if r['note']: md.append('  '+r['note'])
            if r['source']:
                title,url=SOURCES[r['source']]; md.append(f'  [{title}]({url})')
        md += ['',day['dinner']] if day['dinner'] else ['']
        md += [f'\n**{title}:** {prose}' for title,prose in day['notes']]
        md.append('')
    md += ['## Where to stay','']
    for t,p,n in HOTELS: md += [f'### {t}','',p,'',n,'']
    md += ['Property shortlist: [Residence Agnes](https://www.residenceagnes.com/standard-room), [Hotel Josef](https://www.hoteljosef.com/rooms-overview/), [Hotel Haštal](https://www.hastal.com/en/). Rates and availability not checked.','', '## Transport and costs','']
    for t,p in TRANSPORT: md += [f'**{t}:** {p}','']
    md += ['2026 adult fares in CZK:','', '| Validity | App / adult | App / two | Paper / adult |','| --- | ---: | ---: | ---: |']
    md += ['| '+' | '.join(cells)+' |' for cells in FARES]
    md += ['', 'Car budget per vehicle for two: CZK 120–250 short central hops; CZK 200–400 cross-city; CZK 450–800 airport each way. Estimates, not live quotes or caps. Funicular single CZK 90 app / 100 paper; included in 24-hour and 72-hour tickets.', '', '## Selected markets','']
    for n,why,dates,day,s in MARKETS: md += [f'- {n}: {why}. {dates}; {day}.']
    md += ['', 'Four selected markets, not a claim about the total citywide count. Two principal public botanical gardens are included: Troja (Fata Morgana is part of it) and Charles University. Waldstein Garden is closed in December.', '', '## Booking priorities','']
    for w,t,p,s in BOOKINGS: md += [f'- **{w}: {t}.** {p}']
    md += ['', '## Pending checks',''] + ['- '+p for p in PENDING]
    md += ['', '## Sources',''] + [f'- [{t}]({u})' for t,u in SOURCES.values()]
    (ROOT/'itinerary.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
    print('Built index.html and itinerary.md')

if __name__ == '__main__':
    build()

"""Render the route-only page and matching Markdown document."""
from pathlib import Path
from html import escape as e
from urllib.parse import urlencode
from content import DAYS, HOTEL, BOOKINGS, MARKETS, SOURCES, UPDATED, CZK_NIS, USD_NIS

ROOT = Path(__file__).resolve().parent

def price(amount, currency='CZK', upper=None):
    rate = CZK_NIS if currency == 'CZK' else USD_NIS
    original = f'{amount:,}' + (f'–{upper:,}' if upper is not None else '')
    converted = f'{round(amount*rate):,}' + (f'–{round(upper*rate):,}' if upper is not None else '')
    return f'{currency} {original} (≈NIS {converted})'

def transfer(r):
    if not r['high']: return r['mode'] + '; no separate transfer'
    span = str(r['low']) if r['low'] == r['high'] else f"{r['low']}–{r['high']}"
    return f"{r['mode']} · {span} min"

def link(key, label=None):
    title,url = SOURCES[key]
    return f'<a href="{e(url, quote=True)}">{e(label or title)}</a>'

def maplink(r):
    return 'https://www.google.com/maps/search/?' + urlencode({'api':1,'query':r['target']})

def block(title, prose):
    return f'<div class="info"><b>{e(title)}.</b> {e(prose)}</div>'

def day_html(day, number):
    rows = []
    for r in day['rows']:
        rows.append(f'''<li><div><span class="place">{e(r['name'])}</span> <span class="type">({e(r['kind'])})</span><br>
        <span class="transfer">{e(transfer(r))}</span><p class="detail">{e(r['text'])}</p>
        {f'<p class="note">{e(r["note"])}</p>' if r['note'] else ''}
        <div class="links"><a href="{e(maplink(r), quote=True)}">Map pin</a></div></div></li>''')
    notes = ''.join(block(t,p) for t,p in day['notes'])
    dinner = f'<p class="dinner">{e(day["dinner"])}</p>' if day['dinner'] else ''
    return f'''<article class="day" id="{day['id']}"><header class="day-head"><div class="daynum">{number}</div>
    <div><div class="date">{e(day['label'])}</div><h2>{e(day['title'])}</h2></div></header>
    <p class="intro">{e(day['intro'])}</p><ol class="schedule">{''.join(rows)}</ol><div class="day-bottom">{dinner}{notes}</div></article>'''

TRANSPORT = [
 ('Walk short hops; save time on longer ones', 'Walk short central hops, normally up to about 22 minutes, allowing more for hills. For longer journeys, compare Bolt / Uber with public transport door to door, including collection, walking, waits and any traffic. A meaningful time saving is worth paying for; public transport is not compulsory just because it is cheaper.'),
 ('Where cars make sense', 'Bolt is the chosen transfer for both airport journeys. Use Bolt / Uber for both Troja legs. For the Castle or other longer hops, use the live comparison: roughly 15–20 minutes saved is a useful practical guide, not a rigid rule. A car is not automatically quicker in the pedestrianised centre, and there is no reason to drive a short walk. No car hire is needed.'),
 ('Which tickets to buy', f'Use singles on walking-heavy days. On the Petřín day, a 24-hour app ticket costs {price(140)} per person and includes both funicular rides. A 72-hour app ticket costs {price(340)} per person; buy it only if you expect enough journeys to justify it.'),
 ('Airport journeys by Bolt', 'Allow 40–65 min from the arrivals pickup process to Jungmann Hotel after collecting bags, and 45–65 min from hotel pickup access to the departure terminal. These include collection and any short access walk; the drive itself is roughly 30–45 min. Follow the app’s airport meeting point and confirm legal vehicle access near the hotel. Select a car with enough luggage capacity; live traffic, collection and fare estimates override these planning ranges.'),
]
FARES = [('30 minutes',36,72,39),('90 minutes',46,92,50),('24 hours',140,280,150),('72 hours',340,680,350)]
CAR = [
 f'Short central journey: {price(120, upper=250)} per car.',
 f'Longer cross-city journey: {price(200, upper=400)} per car.',
 f'Airport, each way: {price(450, upper=800)} per car.',
 'These are budgeting estimates for both of you together, not live quotes or caps. Check the app total before ordering; surge pricing can cost more.',
]
ON_DAY = 'Buy the Castle circuit, Lobkowicz Palace, Jewish Town circuit, ordinary Troja garden admission, Petřín Tower and St Nicholas Church tickets there. Public transport is also bought as needed; the two markets need no admission ticket. On-site purchase may involve a queue, so check daily access before setting out.'
FX_NOTE = f'NIS equivalents are approximate, rounded using CZK 1 ≈ NIS {CZK_NIS} and USD 1 ≈ NIS {USD_NIS}, checked {UPDATED}. December rates and card fees may differ.'

def build():
    nav = ''.join(f'<a href="#{d["id"]}">{e(d["label"])}</a>' for d in DAYS)
    overview = ''.join(f'<a href="#{d["id"]}">{e(d["label"].split(" · ")[0])} {d["date"][-2:]}</a><span>{e(d["title"])}</span>' for d in DAYS)
    bookings = ''.join(f'<div class="booking"><span class="when">{e(w)}</span><h3>{e(t)}</h3><p>{e(p)}</p>{link(s) if s else ""}</div>' for w,t,p,s in BOOKINGS)
    markets = ''.join(f'<div class="panel"><h3>{e(n)}</h3><p>{e(why)}</p><p class="small">{e(dates)}<br>{e(day)}</p></div>' for n,why,dates,day in MARKETS)
    fares = ''.join('<tr><td>'+e(label)+'</td>'+''.join(f'<td>{e(price(x))}</td>' for x in values)+'</tr>' for label,*values in FARES)
    transports = ''.join(f'<h3>{e(t)}</h3><p>{e(p)}</p>' for t,p in TRANSPORT)
    car = ''.join(f'<p>{e(p)}</p>' for p in CAR)
    flight_summary = 'Flight dates: Tel Aviv to Prague on 18 December; Prague to Tel Aviv on 24 December 2026. Airline and clock times are provisional pending ticket confirmation. Check the issued tickets for the final baggage allowance and fare conditions.'
    intro = 'Stops are listed in visiting order, without a daily timetable or visit durations. All hotel transfers use Jungmann Hotel, Jungmannovo náměstí 2. Transfer ranges include ordinary waits where indicated and are estimates, not measured routes. Enjoy a calm breakfast and a late-morning start; choose any booked tours to suit that pace. Departure day is the early-start exception.'
    html = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Prague, 18–24 December 2026: a route for two with transfer times, Troja Botanical Garden, two Christmas markets and shopping.">
<title>Prague</title><style>{(ROOT/'style.css').read_text()}</style></head><body>
<a href="#itinerary" class="skip">Skip to itinerary</a>
<header class="masthead container"><div class="eyebrow">18–24 December 2026</div><h1>Prague</h1>
<div class="actions"><a href="itinerary.md">Plain-text itinerary</a><a href="https://github.com/oyaMnahtanoJ/prague">GitHub</a><button type="button" onclick="window.print()">Print / save PDF</button></div></header>
<nav class="jump" aria-label="Jump to day or planning section"><div class="container">{nav}<a href="#stay">Stay</a><a href="#transport">Transport</a><a href="#book">Must book</a></div></nav>
<main class="container" id="itinerary"><section aria-labelledby="week"><h2 id="week">The week at a glance</h2><div class="panel overview">{overview}</div><p class="small">{e(intro)}</p><p class="small">{e(flight_summary)}</p></section>
{''.join(day_html(d,i) for i,d in enumerate(DAYS,1))}
<section id="stay"><h2>Your hotel</h2><div class="panel"><h3>{e(HOTEL[0])}</h3><p>{e(HOTEL[1])}</p><p class="small">{e(HOTEL[2])}</p></div></section>
<section id="markets"><h2>The two Christmas markets</h2><div class="grid">{markets}</div></section>
<section id="transport"><h2>Getting around, and what it costs</h2><p class="lede">Take Bolt / Uber when it saves meaningful time. Walk the compact centre; use public transport where it is equally quick or more direct.</p><div class="panel">{transports}<p class="small">{link('fares')} · {link('pid')} · {link('funicular')}</p></div>
<div class="panel"><h3>Public transport fares</h3><div class="table-scroll"><table><thead><tr><th scope="col">Validity</th><th scope="col">App / adult</th><th scope="col">App / two adults</th><th scope="col">Paper / adult</th></tr></thead><tbody>{fares}</tbody></table></div>
<p class="small">Ticket validity is shown here, not a suggested visit duration. Petřín is included in 24-hour and 72-hour tickets, but not ordinary 30-minute or 90-minute tickets. A standalone funicular ride costs {e(price(90))} in the app or {e(price(100))} otherwise, per person, one way.</p>
<h3>Car budgeting, per vehicle</h3>{car}<p class="small">{e(FX_NOTE)} {link('czk-rate')} · {link('usd-rate')}</p></div></section>
<section id="book"><h2>Must book ahead, and when</h2><p class="lede">The short advance-booking list for this plan. Buy the other admission tickets there.</p><div class="panel">{bookings}</div><div class="panel"><h3>Everything else: buy there</h3><p>{e(ON_DAY)}</p></div></section>
</main><footer class="footer"><div class="container">Prague · 18–24 December 2026</div></footer></body></html>'''
    (ROOT/'index.html').write_text('\n'.join(line.rstrip() for line in html.splitlines())+'\n', encoding='utf-8')
    md=['# Prague','','18–24 December 2026','',intro,'',flight_summary,'']
    for day in DAYS:
        md += [f'## {day["label"]}: {day["title"]}','',day['intro'],'']
        for r in day['rows']:
            md += [f'- **{r["name"]}** ({r["kind"]}); {transfer(r)}.',f'  {r["text"]}']
            if r['note']: md.append('  '+r['note'])
        if day['dinner']: md += ['',day['dinner']]
        md += [f'\n**{t}:** {p}' for t,p in day['notes']]
        md.append('')
    md += ['## Your hotel','',f'### {HOTEL[0]}','',HOTEL[1],'',HOTEL[2],'','## The two Christmas markets','']
    md += [f'- {n}: {why} {dates}; {day}.' for n,why,dates,day in MARKETS]
    md += ['','## Transport and costs','']
    for t,p in TRANSPORT: md += [f'**{t}:** {p}','']
    md += ['| Validity | App / adult | App / two | Paper / adult |','| --- | --- | --- | --- |']
    md += ['| '+label+' | '+' | '.join(price(v) for v in values)+' |' for label,*values in FARES]
    md += ['',f'Funicular one-way: {price(90)} in the app or {price(100)} otherwise, per person; included in 24-hour and 72-hour tickets.','']
    md += CAR+['',FX_NOTE,'','## Must book ahead, and when','']
    for w,t,p,s in BOOKINGS:
        md += [f'- **{w}: {t}.** {p}']
        if s: md.append(f'  [{SOURCES[s][0]}]({SOURCES[s][1]})')
    md += ['','### Everything else: buy there','',ON_DAY,'']
    (ROOT/'itinerary.md').write_text('\n'.join(md),encoding='utf-8')
    print('Built index.html and itinerary.md')

if __name__ == '__main__': build()

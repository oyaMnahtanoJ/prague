"""Route in visiting order; durations describe transfers only."""
UPDATED = '23 September 2026'
BASE = 'Jungmann Hotel, Jungmannovo náměstí 2, 110 00 Prague, Czech Republic'
CZK_NIS = 0.1413
USD_NIS = 3.017
SOURCES = {
 'municipal': ('Book an English tour', 'https://www.obecnidum.cz/en/tours/'),
 'hall': ('Old Town Hall tickets', 'https://prague.eu/en/objevujte/old-town-hall-with-astronomical-clock-staromestska-radnice-s-orlojem/'),
 'troja': ('Garden information', 'https://www.botanicka.cz/pro-navstevniky/zakladni-informace/oteviraci-doba.html'),
 'crystal': ('Crystal Garden programme', 'https://www.botanicka.cz/en/articles/events/what-s-on-this-year'),
 'fares': ('PID fares', 'https://pid.cz/en/tickets-and-fare/'),
 'pid': ('Journey planner', 'https://pid.cz/en/'),
 'funicular': ('Funicular information', 'https://pid.cz/en/funicular/'),
 'czk-rate': ('CZK / NIS rate', 'https://wise.com/us/currency-converter/czk-to-ils-rate'),
 'usd-rate': ('USD / NIS rate', 'https://wise.com/us/currency-converter/usd-to-ils-rate'),
}

def row(name, kind, mode, low, high, text, note='', target=None, cover=()):
    return dict(name=name, kind=kind, mode=mode, low=low, high=high, text=text,
                note=note, target=target or name+', Prague', cover=list(cover))

DAYS = [
 dict(id='d1', date='2026-12-18', label='Fri · 18 Dec', title='Flight to Prague; settle in',
      intro='Flight to Prague on 18 December. Provisional airline and times: Smartwings, TLV 18:25 → PRG 21:35, local times. Confirm against the issued ticket. No sightseeing on arrival.',
      rows=[row('Jungmann Hotel','hotel','Bolt, including collection and final access walk',40,65,
                'After passport control and collecting your bags, order Bolt to Jungmannovo náměstí 2. Follow the pickup point shown in the app; the official airport taxi rank is not necessarily the Bolt meeting point. Allow roughly 30–45 min driving, plus collection and any short walk from a legal drop-off.',
                'The transfer range starts after baggage collection, not at landing. Confirm late check-in and access if delayed. Choose a car that fits both travellers and your actual suitcases; eat before flying or arrange a late snack.',target=BASE)],
      dinner='A snack at the hotel if needed.', notes=[]),
 dict(id='d2', date='2026-12-19', label='Sat · 19 Dec', title='Hradčany, the Castle and Lobkowicz',
      intro='Breakfast at leisure. Approach the Castle from the west, then work east through the complex.',
      rows=[
       row('Hradčanské náměstí','historic square / Hradčany district','walk + tram + walk',35,50,
           'From Jungmann Hotel, walk 5–7 min to Národní třída and take tram 22 towards Pohořelec, then walk 10–12 min downhill through Hradčany to the square. The total includes the tram ride and an ordinary wait; check the day’s routing before leaving.',
           'Bolt to a legal Hradčanské náměstí drop-off takes approximately 25–40 min including collection. Choose it if the live door-to-door comparison shows a meaningful saving; otherwise the tram route is straightforward.',cover=('hradcany',)),
       row('St Vitus Cathedral','cathedral interior','walk + entry allowance',10,15,
           'Enter the Castle complex and visit the ticketed cathedral interior. Buy the Castle circuit ticket once.',
           'Services can restrict entry. Visit the Castle interiors before the separately ticketed Lobkowicz Palace, which normally closes later.',cover=('castle','vitus')),
       row('Old Royal Palace','palace interior','walk',3,5,'Vladislav Hall and the historic rooms on the Castle circuit.'),
       row('Lunch near Jiřské náměstí','meal','walk',3,5,'Stay within or immediately beside the Castle complex.',target='Jiřské náměstí Prague'),
       row('St George’s Basilica','basilica interior','walk',3,5,'The Romanesque interior on the Castle circuit.'),
       row('Golden Lane','historic lane / interiors','walk',3,5,'Explore the small houses and displays before the Castle interiors close.'),
       row('Lobkowicz Palace','palace museum','walk',5,10,'Family history, paintings and musical manuscripts, with an audio guide. Separate admission from the Castle circuit.',cover=('lobkowicz',)),
       row('Old Town Square Christmas Market','Christmas market','downhill walk + tram + walk',30,45,
           'Descend towards Malostranská, take a suitable tram towards Old Town, then walk to Staroměstské náměstí for the tree, stalls and illuminated façades.',
           'If the Castle stairs are slippery, return to the Castle tram stop or use a car from a legal road pickup.',cover=('old-market',)),
      ], dinner='Evening: choose dinner on the Old Town route towards Jungmann Hotel, about 5–10 min from the market, then roughly 5–10 min to the hotel depending on the restaurant. Directly from Old Town Square to the hotel: walk 8–12 min.',
      notes=[('Saturday routing','The Jewish Museum is closed on Saturdays. Saturday also avoids the cathedral’s later Sunday tourist opening.')]),
 dict(id='d3', date='2026-12-20', label='Sun · 20 Dec', title='Troja, Old Town Hall and the Clock',
      intro='Troja takes no more than half the day, including travel. Return directly to Old Town for lunch, the Town Hall interiors and the square; no hotel break is built in.',
      rows=[
       row('Fata Morgana, Prague Botanical Garden','tropical greenhouse','Bolt / Uber, including collection and entry walk',30,45,
           'From Jungmann Hotel, use the app’s legal pickup point and go directly to the Fata Morgana entrance at Trojská 750/194. Focus on the greenhouse rather than trying to cover the entire garden.',
           'Public transport takes approximately 50–70 min via metro A from Můstek, metro C from Muzeum to Nádraží Holešovice, then a bus and walking. A car is the planned time-saving option. The greenhouse is closed on Mondays.',target='Fata Morgana Trojská 750/194 Prague',cover=('troja','fata')),
       row('Troja outdoor collections','botanical garden / vineyard viewpoint','walk between garden sections',10,15,
           'Make one compact circuit through the ornamental garden towards St Claire’s Vineyard viewpoint. Skip distant collections; this is a short outdoor complement to the greenhouse.',
           'Leave through an open southern exit towards Kovárna for the car back to the centre.',target='Botanická zahrada Praha Kovárna'),
       row('Lunch near Old Town Square','meal','walk to pickup + Bolt / Uber + short walk',30,45,
           'Return straight to the Old Town edge and walk to lunch near the square. Vehicles cannot drop you at every pedestrianised doorway.',
           'Public transport is approximately 45–65 min. Keep the entire Troja outing within half a day, including both journeys; shorten the outdoor circuit first if delayed.',target='Staroměstské náměstí Prague'),
       row('Old Town Hall','historic interiors / tower','walk + entry allowance',5,10,
           'Visit the historical rooms on an English tour and go up the tower. Choose the appropriate combined ticket.',
           'Reserve a Sunday afternoon tour with margin after the garden, transfer and lunch. If no suitable English tour is offered, exchange this block with Tuesday’s Municipal House visit, subject to both programmes.',cover=('hall',)),
       row('Old Town Square and Týn','historic square / church exterior','walk',2,3,
           'Explore Staroměstské náměstí and see the Church of Our Lady before Týn from outside. This is the architectural visit; Saturday is for the Christmas market.',target='Church of Our Lady before Týn Prague',cover=('old-square','tyn')),
       row('Astronomical Clock','clock exterior','walk',2,3,
           'See the dial and façade. Catch the hourly procession if convenient; no need to wait for the next one just for the show.',target='Prague Astronomical Clock',cover=('clock',)),
      ], dinner='Evening: choose dinner towards Jungmann Hotel, approximately 5–10 min on foot, then another 5–10 min to the hotel depending on the restaurant. Directly from the Astronomical Clock to the hotel: walk 8–12 min.',
      notes=[]),
 dict(id='d4', date='2026-12-21', label='Mon · 21 Dec', title='Shopping',
      intro='A full shopping day with no museum reservations. Spend longer wherever you find things you like.',
      rows=[
       row('Wenceslas Square shops','shopping boulevard / bookshops','walk from Jungmann Hotel',2,4,'Enter the lower end of the square via Můstek. Browse uphill along the boulevard and bookshops, including Luxor if desired; Luxor is about another 5–8 min along the square.',target='Můstek Václavské náměstí Prague'),
       row('Lunch near Wenceslas Square','meal','walk',3,5,'An unhurried lunch with no timed attraction afterwards.',target='Václavské náměstí Prague'),
       row('Na Příkopě','shopping street','walk',5,10,'Continue north-east through the shops towards Náměstí Republiky.',target='Na Příkopě Prague'),
       row('Palladium','shopping centre','walk',5,10,'Finish with the broadest selection of indoor shops on the route, with a coffee break whenever you want.'),
      ], dinner='Evening: dinner around Náměstí Republiky or along Na Příkopě towards the hotel, about 5–10 min from Palladium; then approximately 5–15 min to Jungmann Hotel depending on the restaurant. Directly from Palladium to the hotel: walk 15–18 min.',notes=[]),
 dict(id='d5', date='2026-12-22', label='Tue · 22 Dec', title='Jewish quarter and the Municipal House',
      intro='Give the Jewish quarter a substantial morning, then continue through Old Town to the Municipal House. The actual English-tour programme determines the afternoon order.',
      rows=[
       row('Maisel Synagogue','synagogue / museum','walk from Jungmann Hotel',12,16,'Walk north through Old Town towards Maiselova and start the Jewish Town circuit. Buy a combined ticket including the Spanish and Old-New synagogues.',cover=('jewish',)),
       row('Pinkas Synagogue','synagogue / memorial','walk',4,6,'The memorial and exhibitions.'),
       row('Old Jewish Cemetery','historic cemetery','walk / site transition',2,5,'Continue through the cemetery route.'),
       row('Old-New Synagogue','historic synagogue interior','walk',3,5,'Visit the interior using the appropriate combined ticket.'),
       row('Spanish Synagogue','synagogue / museum','walk',5,8,'The richly decorated interior and museum displays.',cover=('spanish',)),
       row('Lunch in Josefov','meal','walk',3,5,'Lunch around Dušní or V Kolkovně.',target='Dušní Prague'),
       row('Celetná and Powder Gate','historic street / gate exterior','walk from Josefov via Old Town',15,20,'Continue through Old Town and east along Celetná to the Powder Gate.',target='Powder Tower Prague'),
       row('Obecní dům, Municipal House','Art Nouveau interior tour','walk',2,5,
           'Take an English guided tour of the interiors.',
           'Reserve an available English tour for Tuesday. If necessary, exchange this visit with Sunday’s Old Town Hall block rather than forcing unavailable slots.',cover=('municipal',)),
      ], dinner='Evening: dinner near Náměstí Republiky or along Na Příkopě towards the hotel, about 5–10 min on foot; then approximately 5–15 min to Jungmann Hotel depending on the restaurant. Directly from the Municipal House to the hotel: walk 12–16 min.',
      notes=[('Jewish Museum circuit','The Jewish Museum consists of several sites, not another building after the synagogues. The five sites above form the planned circuit.')]),
 dict(id='d6', date='2026-12-23', label='Wed · 23 Dec', title='Petřín, Lesser Town, books and Charles Bridge',
      intro='Reach Petřín by funicular, explore Lesser Town, then cross the bridge towards the final Christmas market.',
      rows=[
       row('Petřín Tower','viewing tower','walk + funicular + walk',35,55,
           'From Jungmann Hotel, walk 18–22 min along Národní and across Most Legií to the Újezd funicular entrance. Take the funicular uphill, then walk to the tower. Alternatively, walk 5–7 min to Národní třída and take a suitable tram to Újezd if conditions favour it.',
           'The total includes ordinary funicular waits, not a long queue. Confirm operation before setting out; if suspended, use the Pohořelec / Strahov alternative below. A 24-hour PID ticket covers the funicular and city transport.',cover=('petrin-tower',)),
       row('Petřín Hill','park / viewpoints','local walking',0,0,'Explore the tower surroundings and open paths before descending.',target='Petřín Gardens Prague',cover=('petrin',)),
       row('Lunch at Újezd','meal','walk + funicular downhill + walk',20,30,'Descend to Újezd and have lunch near the lower station.',target='Újezd Prague'),
       row('St Nicholas Church, Malá Strana','Baroque church interior','walk gently uphill',15,20,'The major Lesser Town church on Malostranské náměstí, not the different church in Old Town Square.',cover=('nicholas',)),
       row('Malostranské náměstí and Lesser Town lanes','historic district','local walking',0,0,'Explore the square and nearby lanes towards Mostecká; continue downhill.',target='Malostranské náměstí Prague',cover=('lesser-town',)),
       row('Shakespeare and Sons','bookshop interior','walk downhill',5,8,'Continue directly from the Lesser Town lanes to the English-language shelves at U Lužického semináře 10.',cover=('bookshop',)),
       row('Charles Bridge','historic bridge / riverside views','walk to bridge',3,5,'Cross from Lesser Town to Old Town, pausing for views and photographs. Walking straight across takes about 8–10 min, longer with stops.',cover=('bridge',)),
       row('Wenceslas Square Christmas Market','Christmas market','walk from the Old Town end of the bridge',18,22,'Continue through the Old Town lanes to the lower part of Václavské náměstí for the second main Christmas market.',cover=('wenceslas-market',)),
      ], dinner='Evening: dinner near the lower end of Wenceslas Square, 5–10 min on foot, then approximately 3–10 min back to Jungmann Hotel depending on the restaurant. The hotel is only 2–5 min from the lower-square market area; no metro or car is needed. Pack tonight.',
      notes=[('Poor visibility or suspended funicular','Replace the tower with Strahov Library if the view is obscured or the funicular is not operating. Walk 5–7 min from Jungmann Hotel to Národní třída, take tram 22 to Pohořelec and walk to Strahov, approximately 35–50 min altogether. Allow 20–25 min downhill to Lesser Town for lunch. Standard library tickets offer doorway views into the halls, not access among the books.'),
             ('Waldstein Garden','Closed in December. Petřín provides the outdoor park time instead.')]),
 dict(id='d7', date='2026-12-24', label='Thu · 24 Dec', title='Breakfast, airport and home',
      intro='Flight home on 24 December. Provisional airline and times: Smartwings, PRG 12:45 → TLV 17:35, local times. Confirm against the issued ticket. Have breakfast and check out before the airport transfer.',
      rows=[row('Prague Airport Terminal 1','airport','Bolt, including pickup access and collection',45,65,
                'Take Bolt from Jungmann Hotel to Terminal 1 for the non-Schengen flight to Tel Aviv; reconfirm the terminal on the ticket. Allow roughly 30–45 min driving plus pickup access and collection. Aim to reach the terminal about three hours before departure, or earlier if instructed by the airline.',
                'Begin the pickup process about 4½ hours before departure, leaving contingency beyond the transfer estimate. Confirm the legal pickup point with the hotel and app. Check Christmas Eve breakfast arrangements; this travel day needs an earlier start than sightseeing days. If no driver accepts promptly, ask reception to arrange a taxi rather than consuming the airport margin.',target='Václav Havel Airport Prague Terminal 1')],
      dinner='',notes=[]),
]

HOTEL = (
 'Jungmann Hotel (hotel)',
 'Booked for six nights, 18–24 December 2026. Address: Jungmannovo náměstí 2, 110 00 Prague, Czech Republic. All hotel-related routes use this address. Můstek metro A/B and the lower end of Wenceslas Square are about 2–4 min away on foot; Old Town Square is about 8–12 min, Národní třída tram stop 5–7 min, and Palladium 15–18 min.',
 'Confirm late arrival and access after a flight delay, breakfast availability and the early Christmas Eve checkout. Request a quiet room and confirm the legal Bolt pickup/drop-off point; pedestrian access restrictions may mean a short walk with the bags. Hotel payment, breakfast inclusion and cancellation conditions are those on your reservation, not assumed here.',
)
BOOKINGS = [
 ('When travel is confirmed and the December programme opens', 'Municipal House English tour', 'Reserve a Tuesday tour. Check both this and the Old Town Hall programme before paying; the two visits can exchange days if needed.', 'municipal'),
 ('When travel is confirmed and Sunday slots are available', 'Old Town Hall English tour and tower', 'Reserve a Sunday afternoon tour and a product including the historical interiors and tower. Leave generous margin after Troja, the return journey and lunch.', 'hall'),
 ('1–3 days before departure home', 'Christmas Eve Bolt pickup', 'Check whether Bolt offers a scheduled ride for the hotel pickup and review its conditions; do not assume a reservation guarantees a driver. Otherwise request on the morning with the margin shown on Day 7. Confirm the meeting point with the hotel and keep a reception-arranged taxi as backup.', None),
]
MARKETS = [
 ('Old Town Square', 'The main tree, historic façades and flagship atmosphere.', '28 Nov 2026–6 Jan 2027', 'Saturday evening'),
 ('Wenceslas Square', 'The second main market, combined with the bridge and Old Town approach.', '28 Nov 2026–6 Jan 2027', 'Wednesday evening'),
]
REQUIRED = {'old-square','castle','vitus','bridge','hall','clock',
            'petrin','petrin-tower','lesser-town','lobkowicz','municipal','spanish','jewish',
            'nicholas','tyn','hradcany','old-market','wenceslas-market','troja','fata','bookshop'}

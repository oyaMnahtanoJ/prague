"""Route in visiting order; durations describe transfers only."""
UPDATED = '23 September 2026'
BASE = 'Haštalské náměstí, Prague'
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
      intro='Assumed Smartwings flight: TLV 18:25 → PRG 21:35, local times. No sightseeing on arrival.',
      rows=[row('Hotel in the Haštalská / Náměstí Republiky area','hotel','Bolt / Uber, including collection',40,65,
                'After passport control and collecting your bags, order a car to the hotel.',
                'Confirm late check-in. Eat before flying or arrange a late snack; do not rely on a restaurant kitchen remaining open.',target=BASE)],
      dinner='A snack at the hotel if needed.', notes=[]),
 dict(id='d2', date='2026-12-19', label='Sat · 19 Dec', title='Hradčany, the Castle and Lobkowicz',
      intro='Breakfast at leisure. Approach the Castle from the west, then work east through the complex.',
      rows=[
       row('Hradčanské náměstí','historic square / Hradčany district','walk + tram + walk',35,50,
           'Walk to Dlouhá třída; take a tram towards Malostranská, then tram 22 to Pohořelec. Walk downhill through Hradčany to the square.',
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
      ], dinner='Evening: dinner in Old Town, about 5–10 min on foot from the market; then 5–15 min back to the hotel area.',
      notes=[('Saturday routing','The Jewish Museum is closed on Saturdays. Saturday also avoids the cathedral’s later Sunday tourist opening.')]),
 dict(id='d3', date='2026-12-20', label='Sun · 20 Dec', title='Troja, Old Town Hall and the Clock',
      intro='Troja takes no more than half the day, including travel. Return directly to Old Town for lunch, the Town Hall interiors and the square; no hotel break is built in.',
      rows=[
       row('Fata Morgana, Prague Botanical Garden','tropical greenhouse','Bolt / Uber, including collection and entry walk',25,40,
           'Go directly to the Fata Morgana entrance at Trojská 750/194. Focus on the greenhouse rather than trying to cover the entire garden.',
           'Public transport takes approximately 45–65 min via Nádraží Holešovice; a car meaningfully reduces this cross-city journey. The greenhouse is closed on Mondays.',target='Fata Morgana Trojská 750/194 Prague',cover=('troja','fata')),
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
      ], dinner='Evening: dinner in Old Town, approximately 5–10 min on foot; another 5–15 min back to the hotel area.',
      notes=[]),
 dict(id='d4', date='2026-12-21', label='Mon · 21 Dec', title='Shopping',
      intro='A full shopping day with no museum reservations. Spend longer wherever you find things you like.',
      rows=[
       row('Wenceslas Square shops','shopping boulevard / bookshops','walk from the hotel area',18,22,'Walk south through Old Town. Browse the boulevard and bookshops, including Luxor if desired.',target='Václavské náměstí Prague'),
       row('Lunch near Wenceslas Square','meal','walk',3,5,'An unhurried lunch with no timed attraction afterwards.',target='Václavské náměstí Prague'),
       row('Na Příkopě','shopping street','walk',5,10,'Continue north-east through the shops towards Náměstí Republiky.',target='Na Příkopě Prague'),
       row('Palladium','shopping centre','walk',5,10,'Finish with the broadest selection of indoor shops on the route, with a coffee break whenever you want.'),
      ], dinner='Evening: dinner around Náměstí Republiky or Haštalská, about 5–10 min on foot; another 5–10 min back to the hotel.',notes=[]),
 dict(id='d5', date='2026-12-22', label='Tue · 22 Dec', title='Jewish quarter and the Municipal House',
      intro='Give the Jewish quarter a substantial morning, then continue through Old Town to the Municipal House. The actual English-tour programme determines the afternoon order.',
      rows=[
       row('Maisel Synagogue','synagogue / museum','walk',8,12,'Start the Jewish Town circuit. Buy a combined ticket including the Spanish and Old-New synagogues.',cover=('jewish',)),
       row('Pinkas Synagogue','synagogue / memorial','walk',4,6,'The memorial and exhibitions.'),
       row('Old Jewish Cemetery','historic cemetery','walk / site transition',2,5,'Continue through the cemetery route.'),
       row('Old-New Synagogue','historic synagogue interior','walk',3,5,'Visit the interior using the appropriate combined ticket.'),
       row('Spanish Synagogue','synagogue / museum','walk',5,8,'The richly decorated interior and museum displays.',cover=('spanish',)),
       row('Lunch in Josefov','meal','walk',3,5,'Lunch around Dušní or V Kolkovně.',target='Dušní Prague'),
       row('Celetná and Powder Gate','historic street / gate exterior','walk from Josefov via Old Town',15,20,'Continue through Old Town and east along Celetná to the Powder Gate.',target='Powder Tower Prague'),
       row('Obecní dům, Municipal House','Art Nouveau interior tour','walk',2,5,
           'Take an English guided tour of the interiors.',
           'Reserve an available English tour for Tuesday. If necessary, exchange this visit with Sunday’s Old Town Hall block rather than forcing unavailable slots.',cover=('municipal',)),
      ], dinner='Evening: dinner near Náměstí Republiky, about 5–10 min on foot; another 5–10 min back to the hotel area.',
      notes=[('Jewish Museum circuit','The Jewish Museum consists of several sites, not another building after the synagogues. The five sites above form the planned circuit.')]),
 dict(id='d6', date='2026-12-23', label='Wed · 23 Dec', title='Petřín, Lesser Town, books and Charles Bridge',
      intro='Reach Petřín by funicular, explore Lesser Town, then cross the bridge towards the final Christmas market.',
      rows=[
       row('Petřín Tower','viewing tower','walk + tram + funicular + walk',45,65,
           'Walk to Dlouhá třída, take a suitable tram towards Újezd, then the funicular uphill and walk to the tower.',
           'The transfer includes ordinary waits. A 24-hour PID ticket covers the funicular and city transport.',cover=('petrin-tower',)),
       row('Petřín Hill','park / viewpoints','local walking',0,0,'Explore the tower surroundings and open paths before descending.',target='Petřín Gardens Prague',cover=('petrin',)),
       row('Lunch at Újezd','meal','walk + funicular downhill + walk',20,30,'Descend to Újezd and have lunch near the lower station.',target='Újezd Prague'),
       row('St Nicholas Church, Malá Strana','Baroque church interior','walk gently uphill',15,20,'The major Lesser Town church on Malostranské náměstí, not the different church in Old Town Square.',cover=('nicholas',)),
       row('Malostranské náměstí and Lesser Town lanes','historic district','local walking',0,0,'Explore the square and nearby lanes towards Mostecká; continue downhill.',target='Malostranské náměstí Prague',cover=('lesser-town',)),
       row('Shakespeare and Sons','bookshop interior','walk downhill',5,8,'Continue directly from the Lesser Town lanes to the English-language shelves at U Lužického semináře 10.',cover=('bookshop',)),
       row('Charles Bridge','historic bridge / riverside views','walk to bridge',3,5,'Cross from Lesser Town to Old Town, pausing for views and photographs. Walking straight across takes about 8–10 min, longer with stops.',cover=('bridge',)),
       row('Wenceslas Square Christmas Market','Christmas market','walk from the Old Town end of the bridge',18,22,'Continue through the Old Town lanes to the lower part of Václavské náměstí for the second main Christmas market.',cover=('wenceslas-market',)),
      ], dinner='Evening: dinner nearby, 5–10 min on foot. Return to the hotel area in about 20–25 min on foot, or 15–25 min by metro and walking; pack tonight.',
      notes=[('Poor visibility','Replace the tower with Strahov Library if the view is obscured. Travel via Pohořelec instead, approximately 35–50 min from the hotel area, then allow 20–25 min downhill to Lesser Town for lunch. Standard library tickets offer doorway views into the halls, not access among the books.'),
             ('Waldstein Garden','Closed in December. Petřín provides the outdoor park time instead.')]),
 dict(id='d7', date='2026-12-24', label='Thu · 24 Dec', title='Breakfast, airport and home',
      intro='Assumed Smartwings flight: PRG 12:45 → TLV 17:35, local times. Have breakfast and check out before the airport transfer.',
      rows=[row('Prague Airport Terminal 1','airport','pre-arranged car',30,45,
                'Arrange collection early enough to reach the terminal about three hours before departure. Follow any earlier reporting instruction from the airline.',
                'This travel day requires an earlier start than your sightseeing days. Confirm Christmas Eve breakfast and the pickup beforehand; no city stop on the way.',target='Václav Havel Airport Prague Terminal 1')],
      dinner='',notes=[]),
]

HOTEL = (
 'Haštalská / Haštalské náměstí to Náměstí Republiky',
 'Look in north-eastern Old Town, around Haštalská and the quieter side streets towards Náměstí Republiky. This gives easy access to Old Town Square, breakfast cafés, the Municipal House, shopping, trams and metro B. Most nearby central walks are around 5–10 minutes; routes currently use Haštalské náměstí as the reference point.',
 'Choose a rear or courtyard-facing room off the main tram streets and away from Dlouhá’s bars. Confirm sound insulation, heating, blackout curtains, a lift if needed and late check-in. Ask which way the actual room faces: the address alone does not establish quietness.',
)
BOOKINGS = [
 ('Now', 'Flights and hotel', 'Choose the flight fare deliberately and reserve the six-night hotel on free-cancellation terms where available. Check baggage, refundable deposits, the cancellation deadline and late check-in.', None),
 ('When travel is confirmed and the December programme opens', 'Municipal House English tour', 'Reserve a Tuesday tour. Check both this and the Old Town Hall programme before paying; the two visits can exchange days if needed.', 'municipal'),
 ('When travel is confirmed and Sunday slots are available', 'Old Town Hall English tour and tower', 'Reserve a Sunday afternoon tour and a product including the historical interiors and tower. Leave generous margin after Troja, the return journey and lunch.', 'hall'),
 ('1–3 days before departure home', 'Christmas Eve airport transfer', 'Arrange a reliable pickup with enough margin for the flight. If using an app reservation, check its conditions rather than assuming a driver is guaranteed.', None),
]
MARKETS = [
 ('Old Town Square', 'The main tree, historic façades and flagship atmosphere.', '28 Nov 2026–6 Jan 2027', 'Saturday evening'),
 ('Wenceslas Square', 'The second main market, combined with the bridge and Old Town approach.', '28 Nov 2026–6 Jan 2027', 'Wednesday evening'),
]
REQUIRED = {'old-square','castle','vitus','bridge','hall','clock',
            'petrin','petrin-tower','lesser-town','lobkowicz','municipal','spanish','jewish',
            'nicholas','tyn','hradcany','old-market','wenceslas-market','troja','fata','bookshop'}

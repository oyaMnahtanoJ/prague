# Prague

Public planning itinerary for two, 18–24 December 2026.

- [Live itinerary](https://oyamnahtanoj.github.io/prague/)
- [Plain Markdown version](itinerary.md)

The traveller has booked Jungmann Hotel, Jungmannovo náměstí 2, for six nights and confirmed the flight times: 18 December, TLV 18:25 to PRG 21:35; 24 December, PRG 12:45 to TLV 17:35, all local times. Flight durations are 4 h 10 min outbound and 3 h 50 min return. No airline, final fare or baggage allowance is inferred from the latest ticket details. Airport journeys use Bolt. December English tours remain to be selected. This project has not made any reservations.

## Edit and build

Edit `content.py` for the daily route and bookings, `build.py` for the page structure and planning appendices, and `style.css` for the appearance. Python 3.9 or newer, no dependencies:

```sh
python3 build.py
python3 validate.py
```

Commit the regenerated `index.html` and `itinerary.md` with the sources. GitHub Pages serves the repository root from `main`.

## Verification limits

The page lists stops in order with transfer estimates, not a visit timetable. Flight times remain explicit. The validator checks sight coverage, transfer fields, requested removals, NIS conversion examples, internal anchors and basic markup. It does not certify visit timing, future opening hours, legal road access, queues, ticket availability or actual travel times. Check those against operators before travel. Exchange-rate equivalents are dated estimates, not December guarantees.

The page contains no credentials, booking references or private contact details. The Portugal repository is separate and unchanged.

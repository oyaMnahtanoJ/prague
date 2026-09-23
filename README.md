# Prague

Public planning itinerary for two, 18–24 December 2026.

- [Live itinerary](https://oyamnahtanoj.github.io/prague/)
- [Plain Markdown version](itinerary.md)

Flights are assumptions supplied by the traveller. Nothing has been booked by this project. The provisional base is Haštalské náměstí; the exact hotel and December English tours remain to be selected.

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

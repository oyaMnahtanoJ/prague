# Prague at Christmas

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

The validator checks the modelled upper-bound transfer arithmetic, stated pre-tour buffers, supplied closing times, sightseeing start and end times, requested-sight coverage, airport margin, local flight-time arithmetic, internal HTML anchors and basic markup. It cannot certify future opening hours, legal road access, live queues, ticket availability, the final hotel’s route or completeness of official announcements. Those are manual/source checks, with remaining uncertainties disclosed on the page.

The page contains no credentials, booking references or private contact details. The Portugal repository is separate and unchanged.

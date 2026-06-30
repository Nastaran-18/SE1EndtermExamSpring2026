# 40231453 — SE1 Endterm Practical Submission

Online movie streaming software ("Filimo-like"), client–server architecture,
implementing the design from the theory section (ERD + 4+1 view + 4 design
patterns: Observer, Factory, Facade, Decorator).

## Structure

```
40231453/
├── src/
│   ├── entities/        # classes matching the ER Diagram (User, Profile, Content, ...)
│   ├── services/        # microservices from the Logical View (auth, catalog, payment, streaming, ...)
│   └── patterns/
│       ├── observer.py  # PlaybackSession notifies UI/logger/recommender
│       ├── factory.py   # creates the right DeviceClient per device (mobile/laptop/smart_tv)
│       ├── facade.py    # StreamingFacade unifies auth + subscription + catalog + streaming
│       └── decorator.py # adds subtitles/HD/multi-audio to a VideoStream dynamically
├── tests/
│   ├── unit/             # unit tests per pattern/class
│   └── acceptance/       # acceptance test for the full +1 scenario (login -> stream)
├── scripts/
│   └── coverage_to_csv.py  # converts coverage.json -> coverage.csv for CI
├── requirements.txt
├── Dockerfile
└── coverage.csv          # generated automatically by CI on the `test` branch
```

## Running tests locally

```bash
cd 40231453
pip install -r requirements.txt coverage
PYTHONPATH=. coverage run -m pytest tests/ -v
coverage report
```

## Running with Docker

```bash
cd 40231453
docker build -t streaming-app .
docker run streaming-app
```

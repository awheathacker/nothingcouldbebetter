# Nothing Could Be Better

A dating site for nihilists — because nothing could actually be better.

## Philosophy

Life has no inherent meaning, so why not find someone to stare into the void with? Nothing Could Be Better is a fun, no-strings-attached place for like-minded people to meet and connect.

**No monetization. No ads. No algorithm. Just a place where nothing matters — and that's the whole point.**

## Tech Stack

- **Backend:** Python 3.12 + FastAPI (modular, functional architecture)
- **Frontend:** React SPA (functional components)
- **Database:** SQLite
- **Testing:** pytest-bdd (BDD with Gherkin scenarios)
- **CI/CD:** GitHub Actions

## Features

1. **Landing Page** — Existential taglines, void-themed hero section
2. **User Profiles** — Dread level, favorite nothing, existential bio, quotes
3. **Matching Algorithm** — Compatibility through shared nothingness
4. **Forum/Message Board** — Musings, rants, collective sighs
5. **Gallery** — FLUX.2 generated art of voids, abysses, and cosmic perspectives

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

## BDD Tests

```bash
pytest tests/ -v
```

## License

MIT — though honestly, licenses are also meaningless.

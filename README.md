# Nothing Could Be Better — A Dating Site for Nihilists

> "We are all here on earth to do nothing."

A gathering place for people who believe life has no objective meaning, purpose, or intrinsic value. Find someone to stare into the void with.

## Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + React Router 6 (CRA) |
| **Backend** | FastAPI (Python 3.12) |
| **Data** | In-memory store (SQLite ready) |
| **CI** | GitHub Actions (backend tests + frontend build) |
| **Deploy** | Nginx + uvicorn + systemd |
| **Images** | FLUX.2-dev (DGX Spark, placeholder gradients) |

## Project Structure

```
nothingcouldbebetter/
├── backend/                    # FastAPI backend
│   ├── app.py                   # App factory
│   ├── models/                  # Data models (UserProfile, Match, ForumPost)
│   ├── routes/                  # API routes (landing, profiles, matching, forum)
│   ├── services/                # Business logic (matching algorithm)
│   ├── static/                  # Static assets + images
│   └── store.py                 # In-memory data store
├── frontend/                     # React SPA
│   ├── src/
│   │   ├── components/          # UI components (Navbar, ProfileCard, etc.)
│   │   ├── pages/             # Page components (Home, Profiles, Matches, Forum, About)
│   │   ├── api.js             # API client with React hooks
│   │   ├── index.css         # Dark void theme (CSS variables)
│   │   └── App.jsx          # Router setup
│   └── package.json
├── tests/                         # BDD-style tests (pytest)
├── deploy/                         # Deployment config
│   ├── nginx.conf
│   ├── uvicorn.service
│   └── DEPLOY.md
└── .github/workflows/ci.yml       # CI pipeline
```

## Development

```bash
# Clone
git clone https://github.com/awheathacker/nothingcouldbebetter.git
cd nothingcouldbebetter

# Backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app:app --factory --port 8000 --reload

# Frontend
cd frontend && npm install
npm start  # Proxies API to localhost:8000

# Tests
pytest tests/ -v --tb=short

# Build for production
cd frontend && npm run build
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/landing/taglines` | Existential taglines |
| `GET /api/landing/hero` | Hero section data |
| `GET /api/landing/about` | About page content |
| `GET /api/profiles/` | List all profiles |
| `POST /api/profiles/` | Create profile |
| `GET /api/profiles/{username}` | Get profile |
| `DELETE /api/profiles/{username}` | Delete profile |
| `GET /api/matches/search?username=X` | Find matches |
| `GET /api/forum/` | List forum posts |
| `POST /api/forum/` | Create post |
| `POST /api/forum/{id}/react` | React to post |

## Matching Algorithm

Compatibility scoring considers:
- **Dread level proximity** (up to 0.4)
- **Shared favorite nothing** (up to 0.3)
- **Quote/philosopher overlap** (up to 0.3)

Scores range from 0.0 to 1.0. Matches above 0.6 are considered "compatible."

## Deployment

See [deploy/DEPLOY.md](deploy/DEPLOY.md) for full instructions.

## CI

GitHub Actions runs on every PR:
- **Backend tests** (28 pytest tests)
- **Frontend build** (React SPA compilation)
- **Frontend tests** (12 component tests)
- **Lint** (Python syntax + pytest)

## Image Generation

Placeholder gradient images are in `backend/static/images/`.
To generate real FLUX.2 images (requires DGX Spark):

```bash
python3 generate_images.py
```

Or manually replace files in `backend/static/images/`.

## License

Public domain. Everything is nothing anyway.

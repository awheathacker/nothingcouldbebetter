# Deploying Nothing Could Be Better

## Architecture

```
┌─────────────────────────────┐
│  nothingcouldbebetter.com   │
├─────────────────────────────┤
│  Nginx (port 80/443)        │
│  ├── /         → React SPA │
│  ├── /images/  → Static   │
│  └── /api/     → FastAPI  │
├─────────────────────────────┤
│  uvicorn (port 8000)        │
│  └── FastAPI backend        │
└─────────────────────────────┘
```

## Deployment Steps

### 1. Server Setup (Ubuntu/Debian)

```bash
# Create www directory
sudo mkdir -p /var/www/nothingcouldbebetter
cd /var/www/nothingcouldbebetter
git clone https://github.com/awheathacker/nothingcouldbebetter.git .

# Set up Python venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt

# Build frontend
cd frontend
npm install
npm run build
```

### 2. Nginx Configuration

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/nothingcouldbebetter
sudo ln -s /etc/nginx/sites-available/nothingcouldbebetter /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### 3. Systemd Service

```bash
sudo cp deploy/uvicorn.service /etc/systemd/system/uvicorn-ncbb.service
sudo systemctl daemon-reload
sudo systemctl enable --now uvicorn-ncbb
```

### 4. DNS

Point `nothingcouldbebetter.com` A record to your server IP.

### 5. SSL (Let's Encrypt)

```bash
sudo certbot --nginx -d nothingcouldbebetter.com
```

## Domain

- **Domain:** nothingcouldbebetter.com
- **Provider:** (configure per DNS provider)

## Environment Variables

Create a `.env` file in the project root:

```
DATABASE_URL=sqlite:///data/app.db
SECRET_KEY=your-secret-key
```

## Frontend Build

The React SPA is built into `frontend/build/`. Nginx serves it as static files
with `/` falling back to `index.html`.

```bash
cd frontend
npm run build
# Output: frontend/build/
```

## Backend

The FastAPI backend runs on `http://127.0.0.1:8000` via uvicorn.

```bash
cd backend
source ../.venv/bin/activate
uvicorn app:create_app --factory --port 8000
```

## Static Images

Placeholder gradient images are in `backend/static/images/`.
To generate real FLUX.2 images:

```bash
python3 generate_images.py
```

Or manually replace files in `backend/static/images/`.

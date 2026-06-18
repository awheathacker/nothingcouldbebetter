# Deploying Nothing Could Be Better

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

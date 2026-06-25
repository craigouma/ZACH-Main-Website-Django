# ZACH Main Website

**Zimbabwe Association of Church-related Hospitals**
Official website for ZACH — built with Django 5.2.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11.14 |
| Framework | Django 5.2.10 |
| Frontend | Bootstrap 5.2, Bootstrap Icons, GLightbox |
| Database | SQLite (development & production on shared hosting) |
| Static files | WhiteNoise (CompressedManifestStaticFilesStorage) |
| Rich text | CKEditor 5 |
| Authentication | django-allauth (with MFA support) |
| Package manager | uv |
| Deployment | cPanel shared hosting — Apache + mod_wsgi |

---

## Project Structure

```
zachapplication/
├── config/                  # Django project settings (base/local/production/test)
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── zachmain/
│   ├── users/               # Custom User model, django-allauth integration
│   ├── websiteapp/          # About, Vision, Gallery, Leadership, Contacts, Resources
│   ├── news/                # Articles and Newsletter links
│   ├── programmes/          # Health programme listings with photos
│   ├── membership/          # Member directory and search
│   ├── partners/            # Partner logos and links (infinite-scroll slider)
│   ├── careers/             # Job listings
│   └── contrib/             # Sites framework migration override
├── passenger_wsgi.py        # cPanel entry point (venv re-exec pattern)
├── requirements.txt         # Pinned runtime deps (generated from pyproject.toml)
├── pyproject.toml           # Project metadata and uv dependencies
└── .env.example             # Environment variable template (safe to commit)
```

---

## Local Development Setup

```bash
# 1. Clone the repo
git clone <repo-url>
cd zachapplication

# 2. Install uv if not already present
pip install uv

# 3. Create virtualenv and install all dependencies
uv sync

# 4. Copy the environment template and fill in your values
cp .env.example .env
# Edit .env — at minimum set DJANGO_SECRET_KEY

# 5. Run migrations
python manage.py migrate

# 6. Start the dev server
python manage.py runserver
```

Visit http://127.0.0.1:8000/

> The SQLite database (`db.sqlite3`) is committed to git and already contains
> all seed data (members, partners, programmes, gallery images, etc.).
> Running `migrate` on a fresh clone applies any new migrations without
> losing existing data.

---

## Environment Variables

All variables are set in `.env` (copied from `.env.example`). Never commit `.env`.

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key — long random string, required |
| `DJANGO_DEBUG` | `True` for local dev, `False` in production |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of valid hostnames |
| `DJANGO_SETTINGS_MODULE` | `config.settings.local` (dev) or `config.settings.production` (prod) |
| `DJANGO_ADMIN_URL` | Admin URL path — default `admin/`, production uses `zachmain/` |
| `DATABASE_URL` | SQLite path — `sqlite:///db.sqlite3` for both dev and shared hosting |
| `EMAIL_BACKEND` | `django.core.mail.backends.console.EmailBackend` until SMTP is configured |

---

## Admin Access

| Environment | URL |
|---|---|
| Local | http://127.0.0.1:8000/admin/ |
| Production | https://zach.org.zw/zachmain/ |

Default superuser: **`zvechurch`** (info@zach.org.zw)
Password is set separately — never commit it to the repo.

---

## URL Structure

| URL | Description |
|---|---|
| `/` | Homepage — stats, programmes overview, news, Zimbabwe map |
| `/about-us/` | Who we are — ZACH history and overview |
| `/about-us/vision/` | Vision, Mission & Values (STARCAPE) |
| `/about-us/what-we-do/` | What we do — interactive province map |
| `/about-us/leadership/` | Leadership team |
| `/about-us/gallery/` | Photo gallery with GLightbox lightbox |
| `/about-us/contacts/` | Contact details and Google Map embed |
| `/programmes/` | Redirects → `/programmes/landing/` |
| `/programmes/landing/` | Health programmes listing |
| `/membership/` | Member directory |
| `/membership/benefits/` | Membership benefits |
| `/membership/how-to-join/` | How to become a member |
| `/partners/` | Partner logos — infinite-scroll slider |
| `/news/` | News articles |
| `/news/newsletter/` | Newsletter links |
| `/careers/` | Job listings |
| `/zachmain/` | Django admin (production) |

**Legacy 301 redirects** are in place for all old `/aboutus/` and `/partner/` URLs.

---

## Content Management

All content is managed via the Django admin at `/zachmain/` (production) or `/admin/` (local).

### Add a news article
1. Admin → News → Articles → Add Article
2. Fill in Title, Content (CKEditor), Author, Published Date
3. **Slug auto-populates from the title** — do not edit it manually after saving
4. Upload a cover image (optional)

### Add a programme
1. Admin → Programmes → Programmes → Add Programme
2. Fill in Name, Description, Photo (optional)
3. The programme appears on `/programmes/landing/` immediately

### Add a gallery image
1. Admin → Websiteapp → Gallery Images → Add Gallery Image
2. Upload the image file and add a Title
3. Appears in `/about-us/gallery/` grid and GLightbox

### Add a partner
1. Admin → Partners → Partners → Add Partner
2. Fill in Name, Website URL
3. Logo is optional — if blank, a styled name placeholder renders in the slider

### Add a career listing
1. Admin → Careers → Job Listings → Add Job Listing
2. Fill in Title, Description (full job text), Location, Closing Date, Application Link
3. Check **Is Active** to make it visible on `/careers/`

### Add a newsletter link
1. Admin → News → Newsletters → Add Newsletter
2. Fill in Title, URL (link to the PDF or external newsletter page), Published Date

### Update contact details
Contact details live directly in the template — not via admin:
- **File:** `zachmain/templates/websiteapp/contacts.html`
- Also update the top-bar and footer in `zachmain/templates/base.html`
- Phone, email, and address appear in 3 places: top bar, footer, and JSON-LD schema

### Update mission / vision / values
These live directly in the templates — not via admin:
- Vision, Mission: `zachmain/templates/websiteapp/vision.html`
- STARCAPE values grid: same file, search for `STARCAPE`
- About / founding history: `zachmain/templates/pages/about.html`

---

## Deployment (cPanel Shared Hosting)

The site runs on cPanel shared hosting at zach.org.zw using
Phusion Passenger + Python 3.11.

### Server details
- cPanel user: zach
- App root: /home/zach/zachsite/
- Virtualenv: /home/zach/virtualenv/zachsite/3.11/
- Python binary: /opt/alt/python311/bin/python3.11
- Admin URL (production): https://zach.org.zw/zachmain/

### First-time setup

**1. Open cPanel Terminal**
Log into cPanel at https://zach.org.zw:2083
Search for "Terminal" and open it.

**2. Clone the repo**
Go to cPanel → Git Version Control → Create
  Clone URL: https://github.com/craigouma/ZACH-Main-Website-Django.git
  Repository Path: zachsite
  Repository Name: ZACH-Main-Website-Django

Note: make the GitHub repo public temporarily to clone,
then set it back to private after cloning completes.

**3. Create the virtualenv**
```bash
/opt/alt/python311/bin/python3.11 -m venv \
  /home/zach/virtualenv/zachsite/3.11
source /home/zach/virtualenv/zachsite/3.11/bin/activate
cd /home/zach/zachsite
pip install --upgrade pip
pip install -r requirements.txt
```

**4. Create the .env file**
```bash
cat > /home/zach/zachsite/.env << 'EOF'
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=zach.org.zw,www.zach.org.zw
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_ADMIN_URL=zachmain/
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EOF
```

**5. Run migrations and collect static**
```bash
python manage.py migrate --settings=config.settings.production
python manage.py collectstatic --noinput \
  --settings=config.settings.production
```

**6. Fix passenger_wsgi.py**
```bash
cat > /home/zach/zachsite/passenger_wsgi.py << 'EOF'
import os
import sys

sys.path.insert(0, '/home/zach/zachsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
EOF
```

**7. Set .htaccess in public_html**
```bash
cat > /home/zach/public_html/.htaccess << 'EOF'
PassengerEnabled on
PassengerAppRoot /home/zach/zachsite
PassengerBaseURI /
PassengerPython /home/zach/virtualenv/zachsite/3.11/bin/python3.11
EOF
```

**8. Set permissions and restart**
```bash
chmod 755 /home/zach/zachsite
chmod 644 /home/zach/zachsite/Passengerfile.json
chmod 644 /home/zach/zachsite/passenger_wsgi.py
mkdir -p /home/zach/zachsite/tmp
touch /home/zach/zachsite/tmp/restart.txt
```

Visit https://zach.org.zw — site should be live.

---

### Redeployment (after local changes)

Run these steps in the cPanel Terminal every time you push
updates from local and want to redeploy:

```bash
# 1. Activate virtualenv and go to project
source /home/zach/virtualenv/zachsite/3.11/bin/activate
cd /home/zach/zachsite

# 2. Pull latest code
git pull origin main

# 3. Install new dependencies (only if requirements.txt changed)
pip install -r requirements.txt

# 4. Apply database migrations (only if models changed)
python manage.py migrate --settings=config.settings.production

# 5. Collect static files
python manage.py collectstatic --noinput \
  --settings=config.settings.production

# 6. Restart Passenger
touch /home/zach/zachsite/tmp/restart.txt
```

---

### Troubleshooting

| Problem | Fix |
|---|---|
| Site shows "It works! Python v3.11.15" | passenger_wsgi.py has test content — re-run step 6 above |
| Passenger error #2 (permission denied) | chmod 755 /home/zach/zachsite && chmod 644 Passengerfile.json |
| 500 error after deploy | Run manage.py check locally first; check logs in /home/zach/logs/ |
| Images not loading | Ensure zachmain/media/ was committed to git and pulled to server |
| Static files (CSS/JS) not loading | Re-run collectstatic and touch tmp/restart.txt |
| 401 Unauthorized | Check public_html/.htaccess — remove any AuthType lines |
| Python App GUI errors | Do not use cPanel Python App GUI — use Terminal directly instead |

---

## Outstanding Content from ZACH

The following items are expected from ZACH before the site is fully production-ready:

| Item | Status |
|---|---|
| Full member directory (135+ institutions) | Only 11 loaded (A–C alphabetically) |
| Partner logos zip | 10 new partners show styled name placeholders |
| Board member full names and official photos | Short names only, no photos |
| FAM headshot (Mr Willard Ziki — Finance & Admin Manager) | Shows `bi-person` placeholder icon |
| Lifeline Grant programme photo | No photo — programme has no image |
| Newsletter actual publication dates | Set to 2024-01-01 and 2025-01-01 placeholders |
| Career listings | 1 loaded (One Stop Centre Administrator, closing 24 Jun 2026) |
| Article cover images | 3 articles have blank image fields |

---

## Known Issues / Notes

- `/programmes/` redirects to `/programmes/landing/` (302 — not a bug)
- Partners without logos render a styled purple name placeholder — will be replaced when logos arrive
- Newsletter publication dates are placeholders — update via admin when confirmed
- Two extra programme photos per programme (GlobalVax, HHA, CBIM) are also in the gallery grid
- Admin URL in production is `/zachmain/` (set via `DJANGO_ADMIN_URL` env var)
- `SECURE_SSL_REDIRECT` is intentionally NOT set — cPanel handles HTTPS at the Apache level
- `db.sqlite3` is committed to git for shared-hosting deployment (no shell access for migrations)

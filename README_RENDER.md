Render deployment steps

1. Create a new Web Service on Render (Docker or "Web Service") and connect your repo (or manual deploy).

2. Build command (Render will run this):
   pip install -r requirements.txt

3. Start command (Render will use Procfile by default):
   (Procfile) web: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT

4. Environment variables (in Render dashboard -> Environment):
   - DJANGO_SECRET_KEY: <your secret key>
   - DJANGO_DEBUG: False
   - DJANGO_ALLOWED_HOSTS: your-app.onrender.com (or comma-separated hosts)
   - DATABASE_URL: (optional) if using Postgres on Render; otherwise leave unset to use SQLite (not recommended for production)

5. Static files
   - The app uses WhiteNoise and `STATIC_ROOT = staticfiles`. After build, run:
     python manage.py collectstatic --noinput
   Render's build hooks / start command can include `collectstatic` if desired.

6. Database
   - For production use Postgres (Render provides managed Postgres). Set `DATABASE_URL` accordingly.
   - If you use SQLite, note the filesystem is ephemeral across deploys (not suitable for persistent DB).

7. Migrations and superuser
   - After deployment you can run:
     python manage.py migrate
     python manage.py createsuperuser
   Render allows running one-off commands via their dashboard.

8. Logs
   - Check Render dashboard logs if issues occur.

Notes
- I added `whitenoise` configuration to `config/settings.py` and a `requirements.txt` and `Procfile`.
- Make sure to add `DATABASE_URL` and `DJANGO_SECRET_KEY` in Render's environment settings for production.

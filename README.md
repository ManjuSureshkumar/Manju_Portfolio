# Manju Venkatachalapathi – Portfolio (Django)

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the development server
```bash
python manage.py runserver
```

### 3. Open in browser
Visit: http://127.0.0.1:8000

---

## Project Structure
```
manju_portfolio/
├── manage.py
├── requirements.txt
├── manju_portfolio/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/                # Main app
    ├── views.py              # All content & contact logic
    ├── urls.py
    ├── templates/
    │   └── portfolio/
    │       └── index.html    # Main template (About / Resume / Contact)
    └── static/
        └── portfolio/
            ├── css/style.css
            ├── js/script.js
            └── images/manju-avatar.png
```

## To Update Content
All personal data (skills, experience, education, etc.) is in `portfolio/views.py` in the `context` dict inside the `index()` function – easy to edit.

## To Enable Email on Contact Form
In `portfolio/views.py`, in the `contact()` function, add Django's `send_mail()` call after validating the form data. Add email settings to `settings.py`.

## Production Deployment
- Set `DEBUG = False` in `settings.py`
- Set a strong `SECRET_KEY`
- Run `python manage.py collectstatic`
- Use gunicorn + nginx

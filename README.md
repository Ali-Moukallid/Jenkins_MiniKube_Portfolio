# Portfolio Website

A Django-based portfolio website featuring a professional CV, current work showcase, and collaboration system.

## Features

- Professional CV display
- Current work and research projects showcase
- Collaboration request system with form validation
- Custom Admin dashboard (`/admin-dashboard/`) to view collaboration requests
- Django Admin site (`/admin/`) to manage models and users
- Responsive design with Bootstrap 5
- SQLite database for data storage

## Setup Instructions

1.  Clone the repository (or ensure all files are in your project directory).

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:
    -   Windows:
        ```bash
        venv\Scripts\activate
        ```
    -   Unix/MacOS:
        ```bash
        source venv/bin/activate
        ```

4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5.  Create migration files:
    ```bash
    python manage.py makemigrations portfolio
    ```
    *!!!!!!!!!!!!!!!!!!!!!!Note: If `python manage.py makemigrations` doesn't detect changes, specifically target the app: `python manage.py makemigrations portfolio`*

6.  Apply migrations to create the database tables:
    ```bash
    python manage.py migrate
    ```

7.  Create a superuser for accessing the Django admin site:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email, and password.

8.  Ensure models are registered in `portfolio/admin.py` to appear in the Django admin site.
    *(This was done automatically if you used the provided files)*

9.  Run the development server:
    ```bash
    python manage.py runserver
    ```

10. Access the website:
    -   Main site: `http://localhost:8000/`
    -   Current Work: `http://localhost:8000/current-work/`
    -   Collaborate (Form): `http://localhost:8000/collaborate/`
    -   Custom Admin Dashboard (Collaboration Requests List): `http://localhost:8000/admin-dashboard/`
    -   Django Admin Site (Manage Models/Users): `http://localhost:8000/admin/`

## Project Structure

-   `portfolio_project/` - Main project directory
    -   `settings.py` - Project settings
    -   `urls.py` - Main URL configuration
    -   `wsgi.py` - WSGI configuration for production
    -   `asgi.py` - ASGI configuration for async support
-   `portfolio/` - Main application directory
    -   `models.py` - Database models
    -   `views.py` - View functions
    -   `forms.py` - Form definitions
    -   `urls.py` - App URL routing
    -   `admin.py` - Admin site configurations
-   `templates/` - HTML templates
    -   `portfolio/` - App-specific templates
        -   `base.html` - Base template with common layout
        -   `home.html` - Home page with CV
        -   `current_work.html` - Projects showcase
        -   `collaborate.html` - Collaboration form
        -   `admin_dashboard.html` - Custom admin view
-   `static/` - Static files (CSS, JS, images)
-   `media/` - User-uploaded files
-   `manage.py` - Django's command-line utility
-   `requirements.txt` - Project dependencies

## Deployment

For production deployment:

1.  Update `settings.py`:
    -   Set `DEBUG = False`
    -   Configure `ALLOWED_HOSTS`
    -   Set a secure `SECRET_KEY`
    -   Configure static and media file serving

2.  Use a production-grade web server (e.g., Gunicorn) with the WSGI configuration:
    ```bash
    gunicorn portfolio_project.wsgi:application
    ```

3.  Set up a reverse proxy (e.g., Nginx) to serve static files and handle SSL.

## Technologies Used

-   Django 5.0.2
-   Bootstrap 5
-   Font Awesome
-   SQLite3
-   Python 3.x

## Security Notes

-   The project uses Django's built-in security features
-   CSRF protection is enabled
-   Form validation is implemented
-   Admin interface is protected by authentication
-   Sensitive data is stored securely in the database

## Contributing

1.  Fork the repository
2.  Create a feature branch
3.  Commit your changes
4.  Push to the branch
5.  Create a Pull Request "# Jenkins_MiniKube_Portfolio" 

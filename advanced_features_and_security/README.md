
# Security Enhancements

## Security Configurations (settings.py)
- DEBUG set to False in production.
- Added browser protection headers:
    - SECURE_BROWSER_XSS_FILTER
    - X_FRAME_OPTIONS
    - SECURE_CONTENT_TYPE_NOSNIFF
- Enforced secure cookies:
    - CSRF_COOKIE_SECURE
    - SESSION_COOKIE_SECURE
- Content Security Policy (CSP) enabled using django-csp.

---

## View Protection
- All forms now include {% csrf_token %}.
- Views use Django ORM instead of raw SQL to prevent SQL injection.
- Input is validated using Django Forms.

---

## Middleware Added
- 'csp.middleware.CSPMiddleware'

---

## Test Cases Performed
- Tested CSRF by attempting form submission without a token.
- Tested SQL Injection using query strings — safely escaped by ORM.
- Tested XSS by injecting <script> tags — blocked by CSP.

---

## Example Commands to Run Project
```bash
# Run project
python manage.py runserver

# Create superuser to access admin (where permissions can be set)
python manage.py createsuperuser

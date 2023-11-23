# yellow-pages

- Functionalities:
- List of Contacts:
    - Display contacts in pages, with each page containing 10 entries.
    - Pagination for easy navigation.
        - Notes. 5 entries in one page.

- User Registration:
    - Allow users to register with the application.
    - User Authentication:
    - Implement user authentication to distinguish between visitors and regular users.
        - Notes. Default Django authentication.

- Contact Management:
    - Visitors can view the list of contacts, and detail of each contact.
    - Registered users can add contacts.
    - Registered users can modify their own contacts.
        - Done.

- Contact Info Form:
    - Implement the contact info form using Django forms.
    - Form should include fields for Phone number, First name, Last name, Address, and Comments.
        - Done.
 

- Database:
    - Choose a database of your own preference (e.g., PostgreSQL, MySQL, SQLite) to store user information and contacts.
        - Notes. pgsql
 

- Backup Job:
    - Schedule a daily job using Celery to back up the database.
        - Notes. schedule cron/celerybeat /5 min  

 

- Technologies:
    -Use Docker for containerization.
    - Django 4.0+ for backend development.
    - Vue JS for the frontend to display the contact list.
    - Celery for scheduling a daily job to backup the database.
        - Notes. Everything in a docker with docker compose (django, db, redis, celery worker, and celery beat services).

- General notes.
    - All env vars are dummy ones.
    - Backend+frontend fully in Django, no Vue.js (widgets???)
    - Still needs to be configured for CI/CD and cloud deployment. -> Tested only locally.
    - Ugly bootstrap UI.
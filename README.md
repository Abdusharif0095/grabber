The web application's functionality is to retrieve information about a specific Android application available on the Aptoide mobile application marketplace (https://en.aptoide.com/) and display it to the user.

# What is inside?
The application is packaged in a Docker container.
# Project Structure
```
.
├── online-store
|     └── main
|     |     └── migrations
|     |     ├── test_data
|     |     ├── __init__.py
|     |     ├── admin.py
|     |     ├── apps.py
|     |     ├── checkers.py
|     |     ├── models.py
|     |     ├── tests.py
|     |     ├── urls.py
|     |     └── views.py
|     ├── online_store
|     |     └── __init__.py
|     |     ├── asgi.py
|     |     ├── settings.py
|     |     ├── urls.py
|     |     └── wsgi.py
|     ├── Dockerfile
|     ├── db.sqlite3
|     ├── docker-compose.test.yml
|     ├── docker-compose.yml
|     ├── manage.py
|     ├── requirements.txt
|     ├── run_app.sh
|     └── run_tests.sh
├── README.md
└── TASK.pdf
```

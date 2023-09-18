The web application's functionality is to retrieve information about a specific Android application available on the Aptoide mobile application marketplace (https://en.aptoide.com/) and display it to the user.

# What is inside?
The application is packaged in a Docker container.
# Project Structure
```
.
├── app - application directory
|     ├── __init__.py
|     ├── api.py - this file contains a script that runs fastapi
|     ├── aptoide.py - this is a dedicated class designed to extract information from the website en.aptoide.com.
|     ├── spider.py - this file contains a class that grabs pages from websites
|     └── test_api.py - pytest file
├── .gitignore - file is used in a Git repository to specify intentionally untracked files or directories that should be ignored by Git
├── Dockerfile - this  is a script containing a collection of commands and parameters used by Docker for automating the process of creating a containerized application
├── README.md - this file describes the project, its purpose, how to set it up, use it, and other pertinent details
├── docker-compose.test.yml
├── docker-compose.yml
├── requirements.txt - list of external dependencies
├── run_app.sh - server startup script
└── run_tests.sh - test run script
```
# To run this Service you should:
- Give permission to execute the script `chmod +x run_app.sh`;
- Run the command `./run_app.sh`;
- After 2 first steps, the application will start listening for requests at `0.0.0.0:8080`.
# To run tests you should follow these commands:
- Give permission to execute the script `chmod +x run_tests.sh`;
- Run the command `./run_tests.sh`.
# Technology stack:
- Docker - is a platform designed to help developers build, share, and run modern applications;
- FastAPI - API web framework.
- beautifulsoup4 - is a Python library for pulling data out of HTML and XML files

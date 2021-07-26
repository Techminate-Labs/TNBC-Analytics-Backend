## Overview
TNBC Analytics tracks the accountability of tnbc government and provides transparency over all the payments.

## Project Setup
Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a GitHub Issue or reach out to any of our communities above.

Clone the project repo.

Set required environment variables:
```shell
# Valid values are development, production, or staging
export DJANGO_APPLICATION_ENVIRONMENT='development'

# A string with random chars
export SECRET_KEY='some random string'
```

Create a virtual environment with Python 3.7 or higher. [Guide](https://docs.python.org/3/library/venv.html)

Install required packages:
```shell
pip3 install -r requirements.txt
```

To initialize the project:
```shell
# create database models
python manage.py migrate

# create super user for admin access
python manage.py createsuperuser

# run the development server
python manage.py runserver
```

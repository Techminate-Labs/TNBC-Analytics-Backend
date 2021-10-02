## Overview
TNBC Analytics tracks the accountability of tnbc government and provides transparency over all the payments.

## Project Setup
Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a GitHub Issue or reach out to any of our communities above.

### Setup cloudinary for images
Create a free account at [Cloudinary](https://docs.python.org/3/library/venv.html)

Take note of your `Cloud Name`, `Api Key`, and  `API Secret` you would need them later

### Clone the project repo.
Fork the project by clicking on the fork button at the top right corner in github, it should then take you to a new repo in your own name. Clone the repo with the code below

`git clone https://github.com/<your_username>/TNBC-Analytics-Backend.git` 

> Change **yourusername** to your github username

**Set required environment variables:**

- Create a `.env` file in the root directory 
```
#./env
# Valid values are development, production, or staging
DJANGO_APPLICATION_ENVIRONMENT=development
SECRET_KEY=some-random-string
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
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

# Collect static files
python manage.py collectstatic

# run the development server
python manage.py runserver
```

## Application Documents:

Architectural Document: https://drive.google.com/file/d/1c37JACKCF4AORYSMUGrK0ZRdPXFEATtZ/view?usp=sharing

ERD: https://drive.google.com/file/d/14HPgb8qW5n6zQitLRaWkDuikcX9tZyc-/view?usp=sharing

Database Design: https://drive.google.com/file/d/1mRUUhH755HjcnaE9bY992LSmNR91GTIj/view?usp=sharing

UML: https://drive.google.com/file/d/1MtgXngOtMxGCDyccR1mQx4-RcLfrSm3n/view?usp=sharing

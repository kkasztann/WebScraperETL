# WebScraperETL
Project description:
In our project we created an app, which allows people to download opinions and info about products, which was searched in Ceneo.pl and export them to the *.csv files. It is possible to run ETL process as well.

## Getting Started
### Prerequisites
In order to start working with the project you need technology for scrapping, such as:
1. Python

### Installation
1. pip install virtualenv
2. . virtualenv
3. . Scripts/activate
4. pip install django
5. pip install requests
6. pip install beautifulsoup4

## Usage
#### Standard procedure to run server:
1. . Scripts/activate
2. cd ../Application
3. python manage.py runserver
#### Database:
1. python manage.py makemigrations
2. python manage.py migrate
Create Admin:
python manage.py createsuperuser






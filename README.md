# Simple REST API endpoints for managing push notifications

## Requirements
python2.7
linux OS
virtualenv
mysql5.6

## To setup project
* create mysql database, ensuring db name and credentials match value in `notification/settings.py`
* setup virtual environment
  * `virtualenv venv`
* Enter virtual environment
  * `source venv/bin/activate`
* Install required packages
  * `pip install -r requirements.txt`

### To run app
* `python manage.py runserver`

* Navigate to 
  * `http://localhost:8000`


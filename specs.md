# Specifications

### Prerequisite
The Sunsplash project requires a prerequisite understanding of the following:
-Django Framework
-Python3.6
-Postgres
-Python virtualenv

## BDD
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View photos of interest | Scroll to see a gallery and click on picture | Displays a picture with name description and copy link for sharing |
| Search a picture by category | Enter the category in the search input| Displays photographs in the searched category |
| View pictures by location | Click on location of interest in menu bar | Displays photographs of chosen location |
| Copy Link to clipboard | Click on copy link button in the modal class | Copies link to clipboard |
| View Single picture | Click on photo of interest then click on image | Displays a single page with details of the picture and related images |





## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations album
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

# Six Sense Mobility Assignment
## Database Used: SQLite
## API made using Django REST Framework (DRF)
## API Endpoints:
## 1. "/": Root URL
 Returns a list of saved data from the database
## 2. "create/": URL to create an entry in Database
Takes JSON Data in the following format:
### { "data": "<data_from_iot_device>" }
Data is saved in SQLite database with a unique ID.
## Installation
Please create a virtual environment and install the necessary modules mentioned in "requirements.txt" file.

Once the modules are installed, you can start the development server provided by Django and test the API endpoints via Postman or any other API testing platform of your choice.
## Other notes
The main code regarding the assignment can be found in the "data" app of this Django project. Please refer to the "models.py" and "views.py" files present in the module.

URL mapping can be found in the "urls.py" file present in project root module.
# ChatApp
Real Time Chat App with emotion Detection using sentiment analysis.

How to Run this application on your machine.

1. Download the project.
2. Install postgreSQL database in your machine.
3. Create a database in postgres named "chatapp" with username = admin and password=admin
4. Now in your working directory create a python3 virtual environment and activate it through command line.
5. After activating the environment, run a command "pip install -r requirements.txt" to install all python libraries required to run this project. You can find requirements.txt file in the project.
5. After this, run command "python manage.py makemigrations" and "python managepy migrate" to create db table schema.
6. To check if schema is created run command "python manage.py dbshell". Now you will see your db "chatapp". Here you can check if tables are created or not.
7. Now Finally to run the project just run command "python manage.py runserver". 

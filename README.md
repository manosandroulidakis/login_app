## Demo Web Application

This app uses Bootstrap, jinja, Fask and a mysql database
to create a login API with the option of password recovery.
In order to interact with the API follow the steps listed below:

1.Clone the github repo, make sure you have Python and SQL server installed

2.open MySQL command line client and create the database by running the following command:

    source path\to\the\file\simple_login\login_query.sql

3.open VScode and create/activate virtual environment and install requirements.txt

4.make sure to enter your sql database credentials at lines 15-17

5.Run app.py

you can visit http://127.0.0.1:5000/ to interact with the API

Keep in mind that the password recovery email might end up in the junk folder.
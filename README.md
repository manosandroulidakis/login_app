## Demo Web Application

This app uses Bootstrap, jinja, Fask and a mysql database
to create a login API with the option of password recovery.

Once you clone the github repo, make sure you have Python and SQL server installed
and follow the steps listed below:

open MySQL command line client
enter your password
run the following command:
    source path\to\the\file\simple_login\login_query.sql

then open VScode and create and activate virtual environment
and install requirements.txt

finally run app.py
(make sure to enter your sql database password at line 16)

you can visit http://127.0.0.1:5000/ to interact with the API

Keep in mind that the password recovery email might end up in the junk folder.
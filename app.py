
import re
import smtplib, ssl 
import MySQLdb.cursors

from flask_mysqldb import MySQL
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for, session
 
 
app = Flask(__name__)
 
app.secret_key = '3Pw13VwNVqpFrfgSxVAoFF88TrCExpGbndQ1KoTgRwxeLl3V3dRH3c6YnBN58OV7'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '31101991'
app.config['MYSQL_DB'] = 'login'
 
mysql = MySQL(app)
 
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        global current_user
        current_user = username
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
 
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
 
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers.'
        elif not username or not password or not email:
            msg = 'Please fill out the form.'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL,% s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered.'
            return render_template('user_registered.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form.'
    return render_template('register.html', msg = msg)

####
@app.route('/form', methods =['GET', 'POST'])
def form():
    msg = ''
    if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'location' in request.form :
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cursor.execute('INSERT INTO inputs VALUES (NULL, % s, % s, % s, % s)', (current_user, first_name, last_name, location, ))
        mysql.connection.commit()
        return render_template('form_completed.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form.'
    return render_template('form.html', msg = msg)


###
@app.route('/password_recovery', methods =['GET', 'POST'])
def password_recovery():    
    if request.method == 'POST' and 'username' in request.form :
        username = request.form['username']
        global current_user
        current_user = username

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT email FROM accounts WHERE username = %s', [username])
        user_email = cursor.fetchone()
        user_email = re.sub("[}:'{!#$]", '', str(user_email))
        user_email = user_email.replace('email ','')

        cursor.execute('SELECT password FROM accounts WHERE username = %s', [username])
        user_password = cursor.fetchone()
        user_password = re.sub("[^0-9]", "", str(user_password))
        
        msg ='message sent'
        if user_email:

            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            receiver_email = str(user_email)
            sender_email = "python.login.app@gmail.com"
            password = 'juylujnydhyzbacn'
            
            text = """This is your password: {fpassword}""".format(fpassword=user_password)
            message = 'Subject: {}\n\n{}'.format('Password Recovery', text)            
            
            message = MIMEText("This is your password: {fpassword}".format(fpassword=user_password))
            message['Subject']= 'Password Recovery'
            message['From'] = sender_email
            message['To'] = receiver_email
            
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, [receiver_email], message.as_string()) 
            
            return render_template('mail_sent.html', msg = msg)
        
    
    return render_template('password_recovery.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
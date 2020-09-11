from flask import Flask, render_template, request, session
from flask import url_for, jsonify, redirect
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV'))

app.config['MAIL_SERVER']='smtp.mail.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ip_profit@mail.ru'
app.config['MAIL_PASSWORD'] = 'aizere2004'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')
    
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    
    if request.method == "POST":
        name = request.form.get('name')
        #change sender to mail that's used to send mails
        sender = 'murat_a@mail.ru'
        sender_email = request.form.get('email')
        rec_email = 'murat_a@mail.ru'
        message_title = 'Message from website by ' + sender_email
        msg = Message(message_title, 
                    sender = sender,
                    recipients = [rec_email])
        msg.body = request.form.get('message')            
        mail.send(msg)
        return redirect('/')

    else:
        return render_template('contact.html')
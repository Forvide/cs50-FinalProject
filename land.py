from flask import Flask, render_template, request, session
from flask import url_for, jsonify, redirect
from flask import send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mail.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 
app.config['MAIL_PASSWORD'] = 
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
        sender = 
        sender_email = request.form.get('email')
        rec_email = 
        message_title = 'Message from website by ' + sender_email
        msg = Message(message_title, 
                    sender = sender,
                    recipients = [rec_email])
        msg.body = request.form.get('message')            
        mail.send(msg)
        return redirect('/')

    else:
        return render_template('contact.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run()

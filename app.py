from flask import Flask
from flask_mail import Mail, Message
from flask import request

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aroldrams@gmail.com'
app.config['MAIL_PASSWORD'] = 'A rams 37'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=['POST'])
def index():
   msg = Message('Hello', sender = 'aroldrams@gmail.com', recipients = ['arnaudrams37@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   print (request)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
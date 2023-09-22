from flask import Flask, request, jsonify
from flask_mail import Message, Mail
from threading import Thread

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_goes_here'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_PORT'] =  587
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'frauddetection001@gmail.com'
app.config['MAIL_PASSWORD'] = 'veryg00d'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_DEFAULT_SENDER'] = 'Credit Card Fraud Detection'
# app.debug = False
mail = Mail(app)

# print(app.config)
def send_email(data):
    """ Function to send emails in the background.
    """
    # print(a)
    with app.app_context():
        msg = Message("Credit Card Fraud Detected",
                    sender="Admin",
                    recipients=[data['email']])
        msg.body = data['message']        
        mail.send(msg)

def send_mail(data):
    Thread(target=send_email, args=(data,)).start()


@app.route('/send_mail', methods=['POST'])
def index():
    data = request.get_json()
    if data['info'] == 'fraud_detected':
        data = {}
        data['email'] = 'sruthy6ps@gmail.com'
        data['message'] = 'Found Credit Card fraud'
        send_mail(data)
    msg = {'msg': 'successfully detected'}

    return jsonify(msg), 200

@app.route('/index')
def text():
    return a

if __name__ == "__main__":
    app.run(debug=True)
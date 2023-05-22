from flask import Flask, render_template, request, redirect
import pickle
from pymongo import MongoClient
from flask_mail import Mail, Message



app = Flask(__name__)


database = {'nachi': '123', 'james': 'aac', 'karthik': 'asdsf'}
@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login',methods=['POST'])
def login():
    print(request.form)
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html')
    else:
        if database[name1]!=pwd:
            return render_template('login.html')
        else:
            return redirect('/index')
        

@app.route('/index')
def home():
    model = pickle.load(open('model.pkl','rb'))
    prediction1=model
    model2 = pickle.load(open('model2.pkl','rb'))
    prediction2=model2
    model3 = pickle.load(open('model3.pkl','rb'))
    prediction3=model3
    return render_template('index.html',prediction1=prediction1,prediction2=prediction2,prediction3=prediction3)


@app.route('/influencer')
def influencer():
    return render_template('dashboard-influencer.html')

@app.route('/finder')
def finder():
    return render_template('influencer-finder.html')


@app.route('/profile')
def profile():
    return render_template('influencer-profile.html')



@app.route('/campaign')
def campaign():
    return render_template('campaign.html')

@app.get('/word')
def word():
    word = pickle.load(open('corpus.pkl', 'rb'))
    return render_template('Senti.html', corpus = word)

@app.route('/demo')
def demo():
    return render_template('map.html')


@app.route('/invoice')
def invoice():
    return render_template('pdf.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'gayathriaids@smvec.ac.in'
app.config['MAIL_DEFAULT_SENDER'] = 'gayathriaids@smvec.ac.in'
app.config['MAIL_PASSWORD'] = 'aids2024'

mail = Mail(app)


@app.route('/email')
@app.route('/', methods=['GET', 'POST'])
def cancel():
    return render_template('inbox.html')


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        subject = request.form['subject']
        msg = Message(subject = subject,
        recipients=[email], body=message)
        mail.send(msg)
        return render_template('email-compose.html', text="Email has been sent")
    

@app.route('/compose')
def compose():
    return render_template('email-compose.html')


@app.route('/about')
def about():
    return render_template('About.html')


@app.route('/contact')
def contact():
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True)

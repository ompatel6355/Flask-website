from flask import Flask,request,redirect,flash
from flask import render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///web.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class web(db.Model):
    sno = db.Column(db.Integer)
    email = db.Column(db.String(200), primary_key = True ,nullable = False, unique=True)
    password = db.Column(db.Integer,nullable = False)
    data_created = db.Column(db.DateTime, default = datetime.utcnow)
    

    def __repr__(self) -> str:
        return f"{self.sno} - {self.email} " 

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = web(sno= '', email= email, password = password)
        db.session.add(data)
        db.session.commit()
        if email and password is None:
            return redirect('/show')
        else:
            return render_template('index.html')
    allAtr = web.query.all()
    return render_template('login.html', allAtr = allAtr)
       

@app.route('/update/<email>')
def update(email):
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        data = web.query.filter_by(email =email).first()
        data.email = email
        data.password= password
        db.session.add(data)
        db.session.commit()
    data = web.query.filter_by(email =email).first()
    return render_template('update.html', data=data)
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/delete/<email>')
def delete(email):
    data = web.query.filter_by(email = email).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/show')

@app.route('/show')
def products():
    allAtr = web.query.all()
    return render_template('show.html', allAtr = allAtr)
    
@app.route('/submit')
def submit():
    return redirect('/')


@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




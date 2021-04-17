from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///df/tmp/web.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class web(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.Integer,nullable = False)
    data_created = db.Column(db.Integer, default = datetime.utcnow)
    

    def __repr__(self):
        return f"{self.sno} - {self.title}" 

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class WinningNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lotnum = db.Column(db.String(50), nullable=False)
    lotalpha = db.Column(db.String(50), nullable=False)
    user_numbers = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    lotterynumber = requests.get('http://lottery_number_api:5000/get_lotterynumbers')
    lotteryalpha = requests.post('http://lottery_alpha_api:5000/get_lotteryalpha', data=lotterynumber.text)
    
    db.session.add(
        WinningNumbers(
            lotnum = lotterynumber.text,
            lotalpha = lotteryalpha.text
        )
    )
    db.session.commit()
    return render_template("index.html", title="Home", lotterynumber=lotterynumber.text, lotteryalpha=lotteryalpha.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
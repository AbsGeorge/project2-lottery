from flask import Flask, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')


db = SQLAlchemy(app)

class WinningNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lotnum = db.Column(db.String(10), nullable=False)
    lotalpha = db.Column(db.String(5), nullable=False)
    player_numbers = db.Column(db.String(10), nullable=False)

@app.route('/', methods=['POST'])
def home():
    entry = request.json["entry"]
    lotterynumber = request.json["number"]
    lotteryalpha = request.json["alphabet"]

    db.session.add(
            WinningNumbers(
                lotnum = lotterynumber,
                lotalpha = lotteryalpha,
                player_numbers = entry
            )
        )
    db.session.commit()

    winning_numbers = lotterynumber + lotteryalpha

    if winning_numbers == entry:
        return Response("You have won £5 million", mimetype='text/plain')
    else:
        return Response("You did not win this time", mimetype='text/plain')

   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
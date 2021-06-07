from flask import Flask 
from flask import render_template, request
import requests
import os 
from os import getenv
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class PlayForm(FlaskForm):
    lottery_numbers  = StringField('Choose Six numbers between 1 and 20',
            validators = [
                DataRequired(),
                Length(min=6, max=6)
                ])
    lottery_alphabets  = StringField('Choose three letters',
            validators = [
                DataRequired(),
                Length(min=3, max=3)
                ])
    submit = SubmitField("Submit" )

app = Flask(__name__)


SECRET_KEY = os.urandom (32)
app.config['SECRET_KEY'] = "fdhalsdjfbrlwiubg"


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def results():

    form = PlayForm()
    
    if request.method == "POST" and form.validate_on_submit():

        lotteryentry = form.lottery_numbers.data + form.lottery_alphabets.data

        lotterynumber = requests.get('http://lottery_number_api:5000/get_lotterynumbers').text
        lotteryalpha = requests.get('http://lottery_alpha_api:5000/get_lotteryalpha').text

        results = requests.post('http://results_api:5000/', json={
            "entry":lotteryentry,
            "number":lotterynumber,
            "alphabet":lotteryalpha
        }).text
    
        winning_numbers = lotterynumber + lotteryalpha
        return render_template("index.html", winning_numbers=winning_numbers, results=results, lotteryentry=lotteryentry)

    elif request.method == "POST":

        raise ValueError(form.errors)

    return render_template("home.html", form=form)



if __name__=='__main__':
    app.run(debug = True, host ='0.0.0.0')
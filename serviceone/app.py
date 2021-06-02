from flask import Flask 
from flask import redirect, render_template, request, url_for
from forms import PlayForm
import requests
import random
import os 
from os import getenv

app = Flask(__name__)


SECRET_KEY = os.urandom (32)
app.config['SECRET_KEY'] = "fdhalsdjfbrlwiubg"


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home')
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
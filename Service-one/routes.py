from flask import render_template
from application import app, db
from application.forms import NameForm
from application.models import Users
import requests

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    userplays = ''
    return_users_numbers = ''
    form = PlayForm()
    
    if form.validate_on_submit():

        lottery_number = form.lottery_number.data
        lottery_alphabets = form.lottery_alphabets.data

        postdata = Users( lottery_number=lottery_number, lottery_alphabets=lottery_alphabets)
        db.session.add(postdata)
        db.session.commit()

from flask import render_template
from application import app, db
from application.forms import NameForm
from application.models import Users
import requests

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    users_playing_numbers = ''
    lottery_number = ''
    form = LotteryForm()
    
    if form.validate_on_submit():

        lotterynumbers = form.lotterynumbers.data
        lotteryalphabets = form.lotteryalphabets.data

        unicode_num_first = requests.post('http://service2:5000', data=lotterynumbers)
        unicode_letter  = requests.post('http://service3:5000', data=lotteryalphabets)
        
        users_playing_numbers = unicode_num_first.text + " " + unicode_letter.text

        lottery_number = requests.post('http://service4:5000', data=users_playing_numbers )

        postData = Users( lotterynumbers=lotterynumbers, lotterynumbers=lotterynumbers, numbers_played=        lottery_number = requests.post('http://service4:5003', data=users_playing_numbers )
.text)
        db.session.add(postData)
        db.session.commit()

    return render_template('home.html', title='Home', form = form,  code = users_playing_numbers, lottery_number = lottery_number)

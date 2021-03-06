from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length



class PlayForm(FlaskForm):
    lottery_numbers  = StringField('Choose Five numbers between 1 and 50',
            validators = [
                DataRequired(),
                Length(min=5, max=5)
                ])
    lottery_alphabets  = StringField('Choose two letters',
            validators = [
                DataRequired(),
                Length(min=2, max=2)
                ])
    submit = SubmitField("Submit" )
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField 
from wtforms.validators import DataRequired, Length

class LotteryForm(FlaskForm):
    lotterynumbers  = StringField('Write 5 randomnumbers',
            validators = [
                DataRequired(),
                Length(min=5, max=5)
                ])
    lotteryalphabets  = StringField('Write 2 random letters',
            validators = [
                DataRequired(),
                Length(min=2, max=2)
                ])
    submit = SubmitField('Get winning numbers')
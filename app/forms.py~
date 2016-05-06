from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired



class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired()]) #DataRequired validates the input to confirm user has submitted 
    remember_me = BooleanField('remember_me', default=False)

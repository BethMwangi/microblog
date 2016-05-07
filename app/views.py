from flask import render_template
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Blossom'}  # fake user
    posts = [  # fake array of posts by users
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Nairobi!' 
        },
        { 
            'author': {'nickname': 'Dee'}, 
            'body': 'The Avengers movie was so cool!' 
        }, 
        {
            'author': {'nickname': 'Boo'},
            'body' : 'Going for pizza today'
        }
        
        
    ]
    return render_template("index.html",
                           title='Home',
                           user = user,
                           posts = posts)
 
# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

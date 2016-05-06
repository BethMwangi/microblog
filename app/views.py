from flask import render_template
from app import app

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

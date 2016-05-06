#!/usr/bin/python

from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
    return 'Hello world'
    

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')
# 0.0.0.0 means webapp is accessible to any device on the web server.


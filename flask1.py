# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask
##### WSGI application
app=Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome to my 1st video on flask on 13 June"

@app.route('/about')
def about():
    return "I am Ayush gupta studying in chandigarh university."
if __name__ == '__main__':
    app.run(debug=True)
    


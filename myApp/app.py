import os
from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('hello.html')

@app.route('/submit', methods=['POST'])
def submit():
    file = request.files['file']

    return redirect('/filteringPage')

@app.route('/filteringPage')
def filterPage():
    return render_template('filtering.html')

@app.route('/filter/<path>')
def submitFilter():
    return render_template('display.html')


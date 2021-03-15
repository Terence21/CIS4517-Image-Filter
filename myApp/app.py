import os
from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_file
)
import s3

app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('hello.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('uploads', f.filename))
        s3.upload_file(f.filename, s3.BUCKET_NAME)
        return redirect('/filteringPage/' + f.filename)

@app.route('/filteringPage/<path>')
def filterPage(path):
    return render_template('filtering.html', path=path)

@app.route('/filter/<path>')
def submitFilter(path, filter_type):
    return render_template('display.html')


@app.route('/download/<filename>', methods=['GET'])
def download(path):
    out = s3.download_file(path, s3.BUCKET_NAME)
    send_file(out, as_attachment= True)

if __name__ == '__main__':
    app.run()


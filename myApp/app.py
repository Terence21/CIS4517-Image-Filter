import os
from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_file
)
import s3_worker

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def homePage():
    return render_template('hello.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('uploads', f.filename.lower()))
        file = request.files['file']
        file.save(os.path.join('downloads', file.filename.lower()))
        s3_worker.upload_file(file.filename.lower(), s3_worker.BUCKET_NAME)
        return redirect('/filteringPage/' + file.filename.lower())


@app.route('/filteringPage/<path>')
def filterPage(path):
    path = path.lower()
    upload = 'uploads/' + path
    return render_template('filtering.html', **locals())


@app.route('/filteringPage/<path>/<filter_type>', methods=['POST'])
def submitFilter(path, filter_type):
    path = path.lower()
    import filters
    filters.imageFilter(path, filter_type)
    #   f = request.files['file']
    # print(f)
    #  s3_worker.upload_file(f.filename.lower(), s3_worker.BUCKET_NAME)
    print('uploaded')
    return render_template('download.html', path=path)


@app.route('/uploads/<path>', methods=['GET'])
def download(path):
    out = s3_worker.download_file(path, s3_worker.BUCKET_NAME)
    path = f'uploads/{path}'
    f = open(path, "rb")
    return send_file(f, attachment_filename=path)


@app.route('/downloads/<path>', methods=['GET'])
def load(path):
    f = open(f"downloads/{path}", "rb")
    return send_file(f, attachment_filename=path, as_attachment=True)



if __name__ == '__main__':
    app.run()

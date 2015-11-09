#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')

import numpy as np 
import os
from datetime import datetime
from flask import Flask, render_template, jsonify, request


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff']


def predict(IMAGE_FILE): 
    result=88

    return result


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            now = datetime.now()
            filename = os.path.join(
                app.config['UPLOAD_FOLDER'],
                "%s.%s" % (now.strftime("%Y-%m-%d-%H-%M-%S-%f"),
                           file.filename.rsplit('.', 1)[1]))
            file.save(filename)
            result = predict(filename) 
            print 'result:', result
            return jsonify({"result": result})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  

    app.run(
        host="0.0.0.0",
        port=8888,
        debug=True
    )

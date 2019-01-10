#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import hashlib

'''
Product name: AirMal-v1.0(仮)
Discription: Malware Ditection System for Mobile Platform
Author: Kusama Yoshiki (nickname:yotti)
'''

UPLOAD_FOLDER = '/Users/JPZ24557/work/SecurityTools/AirMal/v1/tmp' # アップロードしたファイルの置き場所

# ALLOWED_EXTENSIONS = set(['apk','ipa']) # ファイル形式の制限

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 * 1024 # ファイルの最大容量とりあえず50MBにしとく

html = ''' 
    <!doctype html>
    <title>AirMal-v1.0</title>
    <h1>AirMal-v1.0</h1>
    <h3> Mobile Malware Detection System Beta vertion 1.0</h3>
    <h4>現在hashベースのスキャン実装中....</h4>
    <h3>Upload APK or IPA file</h3>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
       ''' 

## hash convert function
def calc_hash(string):

    hash_dict = {
        'md5': hashlib.md5(string).hexdigest(),
        'sha1': hashlib.sha1(string).hexdigest(),
        'sha224': hashlib.sha224(string).hexdigest(),
        'sha256': hashlib.sha256(string).hexdigest(),
        'sha384': hashlib.sha384(string).hexdigest(),
        'sha512': hashlib.sha512(string).hexdigest(),
        }
    return hash_dict

'''
##ファイルの形式の制限 とりあえず、テスト段階なので実装しない(実際には実装済み)
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file: #and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return html


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename) and print("test")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

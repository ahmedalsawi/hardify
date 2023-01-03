import json
import os
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your secret key'
app.config['UPLOAD_FOLDER'] = "tmp"

config = {
    "IP": "172.0.0.1",
    "config": None,
}

"""
Applications template
"""
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/connect',methods=('GET', 'POST'))
def connect():
    if request.method == 'POST':
        ip = request.form['IP']

        f = request.files['file']


        if not ip:
            flash('IP is required!')
        if not f:
            flash('config file required')
        else:
            config['IP'] = ip

            # TODO parse the config and modify as needed
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            fj= open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            config['config'] = json.load(fj)

            # TODO connect to daemon

            return redirect(url_for('board'))
    return  render_template('connect.html')

@app.route('/board',methods=('GET', 'POST'))
def board():
    return render_template('board.html',context={"config":config})



"""
REST APIs
"""

gpio = [
        {"idx":0, "dir": "out", "value":0},
        {"idx":1, "dir": "out", "value":0}
        ]
@app.route('/gpio')
def gpio_get():
    return json.dumps(gpio)

@app.route('/gpio', methods=['POST'])
def gpio_set():
    record = json.loads(request.data)
    # TODO send to daemon to change direction of pin
    # UDP shit goes here
    print(record)
    return jsonify(record)

app.run(debug=True)

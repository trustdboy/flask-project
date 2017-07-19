from flask import Flask, render_template, send_from_directory

import os

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("moorhouseassociates.com" , 1883,60)



app     = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html" , to="Sam Moorhouse"

@app.route('/btn')
def	btn():
	print("button clicked")
	client.publish("test/all", " Trust is walking along the line ")
	return ""

@app.route('/image/<path:path>')
def send_js(path):
    return send_from_directory('image', path)


@app.route('/')
def index():
        return render_template('index.html')


@app.route('/whereami')
def     whereami():
        return "kdua"


@app.route('/hello/<name>')
def	foo(name):
	return render_template('index.html', to=name)

@app.route('/python')
def	dboy():
	return render_template('python.html')


@app.route('/linux')
def	dboy1():
	return render_template('linux.html')




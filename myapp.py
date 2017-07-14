from flask import Flask, render_template, send_from_directory

app	= Flask(__name__)


@app.route('/image/<path:path>')
def send_js(path):
    return send_from_directory('image', path)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/whereami')
def	whereami():
	return "kdua"

if __name__=='__main__':
	app.run(host="0.0.0.0")


from flask import Flask, render_template

templateDir = 'templates\\'
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')
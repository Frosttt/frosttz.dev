from flask import Flask, render_template
import sqlite3

# Set up SQLite connection and create a database
conn = sqlite3.connect('intro_website.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
''')
conn.commit()
conn.close()



templateDir = 'templates\\'
app = Flask(__name__)




@app.route('/')
def index():
	return render_template('index.html')
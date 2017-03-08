from flask import Flask
from flask import render_template

from models.app import Wifi

app = Flask(__name__) #Main Application
app.secret_key = 'josephkagiri'

@app.route('/')
def website_root():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

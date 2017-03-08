from flask import Flask
from flask import render_template

from models.app import Wifi

app = Flask(__name__) #Main Application
app.secret_key = 'josephkagiri'

@app.route('/')
def website_root():
    wifi = Wifi()
    wifi_networks = wifi.Search()

    print(wifi_networks)

    return render_template("index.html", wifi_networks=wifi_networks)

if __name__ == '__main__':
    app.run()

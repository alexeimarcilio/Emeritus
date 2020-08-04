import numpy as np
# import pandas as pd
import folium

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome, Homies!'


if __name__ == '__main__':
    app.run()
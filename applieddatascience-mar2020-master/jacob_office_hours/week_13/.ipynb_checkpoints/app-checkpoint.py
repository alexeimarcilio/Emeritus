import numpy as np
import pandas as pd
import folium

df = pd.read_json('https://data.cityofnewyork.us/resource/sxx4-xhzg.json')
def map_maker(x):
    folium.CircleMarker(location = [x[0], x[1]], radius = 10).add_to(m)

m = folium.Map(location=[40.890848989,-73.864223918])
df[['latitude', 'longitude']].dropna().apply(map_maker, axis = 1)
html_map = m._repr_html_()

arr = np.random.random(size = 6).reshape(3, 2)
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return f'''
#     <h1>Jacob</h1>
#     <p>Welcome to the page, here's my array: {arr}</p>
#     '''

@app.route('/map')
def mapp():
#     return f'''<h1>Maps are cool</h1>
#     <br/>
#     <br/>
#     {html_map}'''
    return render_template('map.html', nyc_map = html_map)






@app.route('/about')
def about():
    return '''
    <h3>About Me</h3>
    <p> I like hot sauce! </p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
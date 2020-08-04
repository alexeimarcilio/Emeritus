from bokeh.models import Slider, ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.plotting import figure
import numpy as np


n_points = 500

data = ColumnDataSource(data = {'x': np.random.random(n_points), 'y': np.random.random(n_points)})

plot = figure(title = 'Random Scatter Plot Generator')

plot.diamond(x = 'x', y = 'y', source = data, color = 'red')


slider_widget = Slider(start = 0, end = 10_000, step = 10, value = n_points)

def callback(attr, old, new):
    points = slider_widget.value
    data.data = {'x': np.random.random(n_points), 'y': np.random.random(n_points)}

slider_widget.on_change('value', callback)

layout = row(slider_widget, plot)

curdoc().add_root(layout)
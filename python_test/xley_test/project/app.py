from flask import Flask, render_template
import pandas as pd

# Import pyxley stuff
from pyxley import UILayout
from pyxley.filters import SelectButton
from pyxley.charts.mg import LineChart, Figure

# Read in the data and stack it, so that we can filter on columns
df = pd.read_csv("fitbit_data.csv")
sf = df.set_index("Date").stack().reset_index()
sf = sf.rename(columns={"level_1": "Data", 0: "value"})

# Make a UI
ui = UILayout(
    "FilterChart",
    "./static/bower_components/pyxley/build/pyxley.js",
    "component_id")

app = Flask(__name__)

# Make a Button
cols = [c for c in df.columns if c != "Date"]
btn = SelectButton("Data", cols, "Data", "Steps")

# Make a FilterFrame and add the button to the UI
ui.add_filter(btn)

# Make a Figure, add some settings, make a line plot
fig = Figure("/mgchart/", "mychart")
fig.graphics.transition_on_update(True)
fig.graphics.animate_on_load()
fig.layout.set_size(width=450, height=200)
fig.layout.set_margin(left=40, right=40)
lc = LineChart(sf, fig, "Date", ["value"], init_params={"Data": "Steps"}, timeseries=True)
ui.add_chart(lc)



sb = ui.render_layout(app, "./static/layout.js")

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template, url_for, request
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import pandas as pd
import pickle
import io
import base64



app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
  return render_template('home.html', title="Home")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/recommend')
def recommend():
  bedroom_options=[1, 2, 3, 4, 5, 6, 7, 8]
  type_options=["Suite", "Whole Apartment", "Giant House"]
  return render_template("recommend.html", bedroom_options=bedroom_options, type_options=type_options)

@app.route('/results', methods=['POST'])
def results():
  try:
    br = int(request.form['bedrooms'])
    nbr = request.form['neighborhood']
    city = request.form['city']
    year = int(request.form['year'])
    airbnb_type = type(request.form['type'])


  except:
    return f"""Uh oh, one of your values was invalid:
              <form action="{url_for('recommend')}">
              <input type="submit" value="Try again" />
              </form>"""

  product = br * year

  fig = Figure()
  ax = fig.subplots()
  ax.set_title("Greatest Graph Ever y=x^2 + 7x + 5")

  x = np.arange(50)
  y = x**2 + 7*x + 5

  ax.plot(x, y)
  ax.set_xlabel("x")
  ax.set_ylabel("y")

  pngImage = io.BytesIO()
  FigureCanvas(fig).print_png(pngImage)

  pngImageB64String = "data:image/png;base64,"
  pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
  #some super great analysis

  return render_template('results.html', product=product, city=city, nbr=nbr, airbnb_type=airbnb_type, image=pngImageB64String)

if __name__=="__main__":
  app.run(debug=True)
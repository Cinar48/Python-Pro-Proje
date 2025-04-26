from flask import Flask, render_template, request
from model import atik_ayristirici
app = Flask(__name__)
# İlk sayfa
@app.route('/')
def index():
    sonuc=atik_ayristirici(image="image.png")
    return render_template('Ana_sayfa.html',sonuc=sonuc)
app.run(debug=True)
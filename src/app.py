from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def documentation():
    return render_template('docs/documentation.html')
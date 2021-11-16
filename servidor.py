# coding= UTF-8
from flask import Flask, render_template, request
import os

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug = True)
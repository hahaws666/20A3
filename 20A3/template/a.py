from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('donating.html')


app.run(host='0.0.0.0', port=81, debug=True)
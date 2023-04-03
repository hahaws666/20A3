from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__,template_folder="template")

@app.route('/')
def home():
    return render_template("donating.html")


app.run()
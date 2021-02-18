from flask import render_template, redirect, url_for, request
from app import app
from app.forms import IndexForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = IndexForm()
    if request.method == 'POST':
        return render_template('index.html', form=form , message = "ABC432132144, Your prize is a Boat!")
    return render_template('index.html', form=form)
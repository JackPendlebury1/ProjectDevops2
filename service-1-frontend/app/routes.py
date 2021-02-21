from flask import render_template, redirect, url_for, request
from app import app
from app.forms import IndexForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = IndexForm()
    if request.method == 'POST':
        char = request.get("http://service2:5001/get_chargen")
        num = request.get("http://service3:5002/get_numgen")
        prize = request.post("http://service4:5003/get_prize", json={"account_number" : char.text + num.text})
        return render_template('index.html', form=form, message = prize.text)
    return render_template('index.html', form=form, message = "")
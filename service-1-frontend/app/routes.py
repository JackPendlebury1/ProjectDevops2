from flask import render_template, redirect, url_for, request
from app import app, db
from app.forms import IndexForm
from app.models import Prizes
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    form = IndexForm()
    if request.method == 'POST':
        char = requests.get("http://service2:5000/get_chargen")
        num = requests.get("http://service3:5000/get_numgen")
        prize = requests.post("http://service4:5000/prize", json={"account_number" : char.text + num.text})

        account_prize = Prizes(account_number = char + num, prize = prize.text)
        db.add(account_prize)
        db.commit()
        prizes = Prizes.query.limit(10).all()
        return render_template('index.html', form=form, message = prize.text, prizes = prizes)
    return render_template('index.html', form=form, message = "")
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
        account_number = char.text + num.text
        account_prize = Prizes(account_number = account_number, prize = prize.text)
        db.session.add(account_prize)
        db.session.commit()
        prizes = Prizes.query.order_by(Prizes.id.desc()).limit(4)
        return render_template('index.html', form=form, message = "your account number is: " + account_number + " and your prize is a " + prize.text, prizes = prizes)
    return render_template('index.html', form=form, message = "")
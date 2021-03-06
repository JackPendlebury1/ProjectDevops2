from flask import render_template, redirect, url_for, request, Response
from app import app
import random

@app.route("/prize", methods=["GET","POST"])
def prize():
    big_prizes = ["Boat", "Car", "£10000", "Laptop", "Bike", "TV"]
    small_prizes = ["Egg", "Salt", "Coal", "£1", "Coffee", "Duck"]
    account_number = request.get_json()
    if account_number["account_number"].startswith(("A", "E", "I", "O", "U")):
        prize = random.choice(big_prizes)
    else:
        prize = random.choice(small_prizes)
    return Response(str(prize), mimetype='text/plain')
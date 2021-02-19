from flask import render_template, redirect, url_for, request, Response
from app import app
import random
import string

@app.route('/get_chargen', methods=['GET'])
def chargen():
    rand = random.randint(2,3)
    final_char = ''
    for i in range(rand):
        char = random.choice(string.ascii_letters)
        i += 1
        final_char += char
    return Response(str.upper(final_char), mimetype ='text/plain')
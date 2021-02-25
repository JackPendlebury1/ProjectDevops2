from flask import render_template, redirect, url_for, request, Response
from app import app
import random
import string

@app.route('/get_numgen', methods=['GET'])
def numgen():
    rand = random.randint(6,8)
    final_num = ''
    for i in range(rand):
        num = random.randrange(0,9)
        i += 1
        final_num += str(num)
    return Response(final_num , mimetype ='text/plain')
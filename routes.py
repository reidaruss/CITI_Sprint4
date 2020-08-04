# from style_transfer import get_styled_image
from flask import Flask
from flask import send_file
from flask import request, session

# from flask_cors import CORS, cross_origin
routes = Flask(__name__)

from flask import request, jsonify, Response, render_template


import numpy as np

import os
import logging
from flask_cors import CORS, cross_origin


@routes.route("/")
def index():
    return "Hello World!"


@routes.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        global styles
        rows = request.form['rows']
        cols = request.form['cols']
        arr = request.form['arr']
        print(arr[0])
        selected_styles = []
        for x in arr:
            if x == ',':
                continue
            selected_styles.append(styles[x])

        global counter
        image_num = str(counter)

        file = request.form['image']

        imgdata = base64.b64decode(file)
        filename = './../IncomingImage' + image_num + '.jpg'

        with open(filename, 'wb') as f:
            f.write(imgdata)

        # output_img = get_styled_image(filename + '.jpg', selected_styles, num_rows=2, num_cols=1)
        # output_img = get_styled_image(filename, selected_styles, num_rows=2, num_cols=1)
        output_img = get_styled_image(filename, selected_styles, num_rows=int(rows), num_cols=int(cols))
        output_img.rotate(270)
        output_img.save('./../returnImage' + image_num + '.jpg')
        counter = counter + 1

        return "done"

    else:
        return "This is a GET bro"


if __name__ == "__main__":
    # routes.run(host='0.0.0.0')
    routes.secret_key = os.urandom(24)
    routes.run(host="0.0.0.0", use_reloader=False)

flask_cors.CORS(routes, expose_headers='Authorization')

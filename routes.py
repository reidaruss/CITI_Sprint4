# from style_transfer import get_styled_image
from flask import Flask
from flask import send_file
from flask import request, session
from flask import jsonify
from plots import run_plots
# from flask_cors import CORS, cross_origin

import chart_studio.tools as tls

routes = Flask(__name__)

from flask import request, jsonify, Response, render_template


import numpy as np

import os
# import logging
# from flask_cors import CORS, cross_origin


@routes.route("/")
def index():
    return "Hello World!"


@routes.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        return "This is a POST"

    else:
        tick = request.args.get('ticker')
        exps = run_plots(tick)
        embeded = tls.get.get_embed('https://www.dropbox.com/s/yszoi5k6cguuc4o/options.html?dl=0')
        return jsonify(exps), jsonify(embeded)


if __name__ == "__main__":
    # routes.run(host='0.0.0.0')
    routes.secret_key = os.urandom(24)
    routes.run(host="0.0.0.0", use_reloader=False)

# flask_cors.CORS(routes, expose_headers='Authorization')

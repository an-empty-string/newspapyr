from flask import Flask, jsonify, request, url_for
import functools
app = Flask(__name__)

def make_routes():
    import importlib
    import os
    for j in [i[:-3] for i in os.listdir(".") if i.endswith(".py") and i != "service.py"]:
        importlib.import_module(j)

def method(route):
    def decorator(f):
        @functools.wraps(f)
        def wrapped():
            return jsonify(f(request.form))
        app.add_url_rule("/" + "/".join(route.split(".")) + "/", f.__name__, wrapped, methods=["POST"])
        return wrapped
    return decorator

import service.views.ping

if __name__ == '__main__':
    app.run(port=4999, debug=True)

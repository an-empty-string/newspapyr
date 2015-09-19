from flask import Flask
app = Flask(__name__)

import newspapyr.api
import newspapyr.views.index

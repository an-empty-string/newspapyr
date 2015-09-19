from flask import render_template, session, request
from newspapyr import app
from newspapyr.api import ApiWrapper

api = ApiWrapper()

app.secret_key = 'DANK MEMES'

def session(uid):
	session['uid'] = uid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register')
def api_register():
	i = request.form.to_dict()
	uid = api.auth.register(username=i["username"], password=i["password"])
	session(uid)
	return "whoooooo, you're registered with uid" + uid

@app.route('/register')
def register():
	return render_template("register.html")
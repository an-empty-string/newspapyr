from flask import render_template, session, request
from newspapyr import app
from newspapyr.api import ApiWrapper

api = ApiWrapper()

#def sessionuid(uid):
#	session['uid'] = uid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def api_register():
	i = request.form
	auth = api.auth.register(username=i["username"], password=i["password"])
	if not auth["success"]:
		return "no"
#	session["uid"] = auth["uid"]
	return "whoooooo, you're registered"

@app.route('/register')
def register():
	return render_template("register.html")
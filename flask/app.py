from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient
import subprocess, bcrypt
#####################################################################

client = MongoClient(host = "localhost", port = 27017)
db = client.Project

#####################################################################
app=Flask(__name__)

## v
@app.route("/")
def index():
	return render_template("index.html")

## get password for run mdadm command as admin
@app.route("/login", methods=["GET", "POST"])
def login():
	# if "email" in session:
	# 	return redirect(url_for("logged_in"))
	if request.method == "GET":
		return render_template("login.html")
	
	email = request.form["email"]
	password = request.form["password"]
	
	# password = request.form["password"]
	#subprocess.Popen("python3 ./mydatabase/test.py", shell=True)
	# return redirect(url_for("index"))


# get password for run mdadm command as admin
@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")
	username = request.form["username"]
	email = request.form["email"]
	password = request.form["password"]
	if len(list(db.USER.find({"email": email}))) > 0:
		msg = "email is used"
		print(len(list(db.USER.find({"email": email}))))
		print(list(db.USER.find({"email": email})))
		return render_template("register.html", msg = msg)
	
	db.USER.insert_one({"username": username, "email": email, "password": bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())})
	return redirect(url_for("index"))



## v
# @app.route("/VMDinfo")
# def vmdinfo():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh VMDinfo.sh " + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		out = out.decode().replace(""", "")
# 		cells = [out.split()]
# 		return render_template("test.html", cells = cells, len = len(cells))
# @app.route("/create-raid")
# def create():
# 	return render_template("create-raid.html")
# ## create volume v
# @app.route("/create-volume")
# def createVolume():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		return render_template("create-volume.html")
# ## volume-validate x
# @app.route("/generate-volume", methods=["POST"])
# def generateVolume():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		validate = subprocess.Popen("sh volume-validate.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		if not validate:
# 			redirect(url_for("create-volume"))
# 		level = request.form["level"]
# 		count = request.form["count"]
# 		volName = request.form["volName"]
# 		disks = request.form["disks"]
# 		out = subprocess.Popen("sh genVolume.sh " + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		out = out.decode().replace(""", "")
# 		return render_template("index.html")

# ## create container v
# @app.route("/create-container")
# def createContainer():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		return render_template("create-container.html")
# ## container-validate x
# @app.route("/generate-container", methods=["POST"])
# def generateContainer():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		# run validate shell
# 		validate = subprocess.Popen("sh container-validate.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		if not validate:
# 			redirect(url_for("create-container"))
# 		# if pass, create raid
# 		out = subprocess.Popen("sh sample.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)

# ## dashboard x
# @app.route("/info")
# def getInfo():
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh example.sh" + password, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)

# ## delete
# @app.route("/delete/<deviceName>", methods=["POST"])
# def delete(deviceName):
# 	if password == None:
# 		return redirect(url_for("getPwd"))
# 	else:
# 		out = subprocess.Popen("sh delete.sh" + password + deviceName, shell=True, stdout=subprocess.PIPE).stdout.read()
# 		return render_template("index.html", out = out)



if __name__ == "__main__":
	app.run(host="127.0.0.1",port="5001",debug=True)
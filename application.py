import os
from flask import Flask, render_template, session, request, redirect
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from collections import deque
from session import login

app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key"
socketio = SocketIO(app)

channels=[]
users=[]
messages=dict()

@app.route("/")
@login
def index():
    return render_template("index.html", channels=channels)

@app.route("/allChannels")
@login
def allChannels():
	return render_template("allChannels.html", channels=channels)

@app.route("/addChannel", methods=["GET", "POST"])
@login
def addChannel():
	newch=request.form.get("channel")
	if request.method=="POST":
		if newch in channels:
			return render_template("error.html", message="Channel already exists")
		channels.append(newch)
		messages[newch]=deque()
		return redirect("/channels/"+newch)
	else:
		return redirect("/")

@app.route("/channels/<channel>", methods=["GET", "POST"])
@login
def channel(channel):
	session["current_channel"]=channel
	if request.method=="POST":
		return redirect("/")
	else:
		return render_template("channel.html", channels=channels, messages=messages[channel])

@app.route("/signin", methods=["GET", "POST"])
def signin():
	session.clear()
	username=request.form.get("username")
	if request.method == "POST":
		if len(username) < 1 or username is '':
			return render_template("error.html", message="Invalid username")
		if username in users:
			return render_template("error.html", message="Username already exists")
		users.append(username)
		session["username"]=username
		session.permanent=True
		return redirect("/")
	else:
		return render_template("signin.html")

@app.route("/logout", methods=["GET"])
def logout():
	try:
		users.remove(session["username"])
	except ValueError:
		pass
	session.clear()
	return redirect("/")

@socketio.on("joined", namespace="")
def joined():
	room=session.get("current_channel")
	join_room(room)
	emit("status",{
		"userJoined": session.get("username"),
		"channel": room,
		"msg": session.get("username")+" has entered"},
		room=room)

@socketio.on("send message")
def send_msg(msg, timestamp):
	room=session.get("current_channel")
	if len(messages[room])>100:
		messages[room].popleft()
	messages[room].append([timestamp, session.get("username"), msg])
	emit("announce message",{
		"user": session.get("username"),
		"timestamp": timestamp,
		"msg": msg},
		room=room)
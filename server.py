import random
import datetime
from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
	if "gold" not in session:
		session["gold"] = 0
	if "activities" not in session:
		session["activities"] = ""
	return render_template("index.html")

@app.route("/process_money",methods=["POST"])
def process():
	time = "({:%Y-%m-%d %I:%M:%S %p})".format(datetime.datetime.now())
	if request.form["building"] == "farm":
		gold_add = random.randrange(10,21)
		session["gold"] += gold_add
		act_add = "You found " +str(gold_add)+ " gold at the farm! " +time+ "\n"
		session["activities"] = act_add + session["activities"]
		print time
		print act_add
		print gold_add
	elif request.form["building"] == "cave":
		gold_add = random.randrange(5,11)
		session["gold"] += gold_add
		act_add = "You found " +str(gold_add)+ " gold in the cave! " +time+ "\n"
		session["activities"] = act_add + session["activities"]
		print gold_add
	elif request.form["building"] == "house":
		gold_add = random.randrange(2,6)
		session["gold"] += gold_add
		act_add = "You found " +str(gold_add)+ " gold in the house! " +time+ "\n"
		session["activities"] = act_add + session["activities"]
		print gold_add
	elif request.form["building"] == "casino":
		gold_add= random.randrange(-50,51)
		session["gold"] += gold_add
		if gold_add >-1:
			act_add = "You won " +str(gold_add)+ " gold at the casino! " +time+ "\n"
			session["activities"] = act_add + session["activities"]
		else:
			gold_add = abs(gold_add)
			act_add = "You lost " +str(gold_add)+ " gold in the casino... Better luck next time. " +time+ "\n"
			session["activities"] = act_add + session["activities"]
		print gold_add


	return redirect("/")
app.run(debug=True)
from flask import *
import pymongo
import pandas as pd

app = Flask(__name__)

# Initialize MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hotel"]
table = db["Rooms"]

data = table.find()

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/menu",methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "admin":
        return render_template("menu.html")
    elif username == "Rahul" and password == "kl.rab_3490":
        return render_template("menu.html")
    else:
        return "Sorry, %s is unable to login" %username

@app.route("/menu-action",methods=['POST'])
def menu():
    choice = request.form['choice']
    if choice == "1":
        return render_template("add.html")
    elif choice == "2":
        return render_template("remove.html")
    elif choice == "3":
        return render_template("update.html")
    elif choice == "4":
        return render_template("display.html",data=data)
    elif choice == "5":
        return render_template("index.html")
    else:
        return render_template("menu.html")

@app.route("/add-data",methods=['POST'])
def add_data():
    roomNo = request.form['roomNo']
    roomUser = request.form['roomUser']
    roomCount = request.form['roomCount']
    roomStay = request.form['roomStay']
    content_add={"RoomID":roomNo,"User":roomUser,"Count":roomCount,"Stay":roomStay}
    x = table.insert_one(content_add)
    data = table.find()
    return render_template("display.html",data=data)

@app.route("/display-data",methods=['POST'])
def display_data():
    data = table.find()
    return render_template("menu.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001)
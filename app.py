from flask import *
import pymongo
import pandas as pd

app = Flask(__name__)
app.secret_key="string"

# Initialize MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hotel"]
table = db["Hotel-Room"]

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
        flash("Sorry Unable To Login")
        return render_template("index.html")

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
        data =table.find()
        return render_template("display.html",data=data)
    elif choice == "5":
        return render_template("index.html")
    else:
        return render_template("menu.html")

@app.route("/add-data",methods=['POST','GET'])
def add_data():
    roomNo = request.form['roomNo']
    roomUser = request.form['roomUser']
    roomCount = request.form['roomCount']
    roomStay = request.form['roomStay']
    content_add={"RoomID":roomNo,"User":roomUser,"Count":roomCount,"Stay":roomStay}
    x = table.insert_one(content_add)
    data = table.find()
    return render_template("display.html",data=data)

@app.route("/remove-data",methods=['POST'])
def remove_data():
    roomNo = request.form['roomNo']
    content_delete = {"RoomID":roomNo}
    delete_data = table.find_one(content_delete)
    if delete_data == None:
        flash("No Such Value Exits")
        return render_template("menu.html")
    else:
        table.delete_one(content_delete)
        data =table.find()
        return render_template("display.html",data=data)

@app.route("/update-data",methods=['GET'])
def update_data():
    roomNo = request.form['roomNo']
    content_find = {"RoomID":roomNo}
    search = table.find_one(content_find)
    if search == None:
        flash("No Data To Update")
        return render_template("menu.html")
    else:
        nroomNo = request.form['nroomNo']
        nroomUser = request.form['nroomUser']
        nroomCount = request.form['nroomCount']
        nroomStay = request.form['nroomStay']
        data = table.find()
        if nroomNo!="":
            table.update_one({"RoomID":roomNo},{"$set":{"RoomID":nroomNo}})
            return render_template("display.html",data=data)
        elif nroomUser!=None and nroomNo==None and nroomCount==None and nroomStay==None:
            table.update_one({"RoomID":roomNo},{"$set":{"User":nroomUser}})
            return render_template("display.html",data=data)
        elif nroomCount!=None and nroomNo==None and nroomUser==None and nroomStay==None:
            table.update_one({"RoomID":roomNo},{"$set":{"Count":nroomCount}})
            return render_template("display.html",data=data)
        elif nroomStay!=None and nroomNo==None and nroomUser==None and nroomCount==None:
            table.update_one({"RoomID":roomNo},{"$set":{"Stay":nroomStay}})
            return render_template("display.html",data=data)
        elif nroomNo!=None and nroomUser!=None and nroomCount!=None and nroomStay!=None:
            table.update_one({"RoomID":roomNo},{"$set":{"RoomID":nroomNo,"User":nroomUser,"Count":nroomCount,"Stay":nroomStay}})
            return render_template("display.html",data=data)
        else:
            flash("No Data Entry")
            return render_template("update.html") 
            
@app.route("/display-data",methods=['POST'])
def display_data():
    data = table.find()
    return render_template("menu.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001)
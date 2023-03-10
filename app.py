# Import Statements
from flask import *   #Flask to make python program to a web-application 
import pymongo # To connect to MongoDB 

# Define Flask app and secret key to show messages in Flask Web
app = Flask(__name__)
app.secret_key="string"

# Initialize MongoDB client
client = pymongo.MongoClient("mongodb+srv://rahulab664:CEZkFDDlOjL253bL@hotel.o79aes9.mongodb.net/?retryWrites=true&w=majority")
db = client["Hotel"]
table = db["Hotel-Room"]

#Main Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

#Login In Check 
@app.route("/menu",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return render_template("menu.html")
        elif username == "Rahul" and password == "kl.rab_3490":
            return render_template("menu.html")
        else:
            flash("Sorry Unable To Login")
            return render_template("index.html")
    
# Menu Section
@app.route("/menu-action",methods=['POST','GET'])
def menu():
    if request.method == 'POST':
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
    
# Adding Data To MongoDB
@app.route("/add-data",methods=['POST','GET'])
def add_data():
    if request.method =='POST':
        roomNo = request.form['roomNo']
        roomUser = request.form['roomUser']
        roomCount = request.form['roomCount']
        roomStay = request.form['roomStay']
        content_add={"RoomID":roomNo,"User":roomUser,"Count":roomCount,"Stay":roomStay}
        x = table.insert_one(content_add)
        data = table.find()
        return render_template("display.html",data=data)

# Removing Data From MongoDB 
@app.route("/remove-data",methods=['POST','GET'])
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

# Updating Data In MongoDB
@app.route("/update-data",methods=['GET','POST'])
def update_data():
    roomNo = request.form['roomNo']
    content_find = {"RoomID":roomNo}
    search = table.find_one(content_find)
    if request.method == 'POST':
        nroomNo = request.form['nroomNo']
        nroomUser = request.form['nroomUser']
        nroomCount = request.form['nroomCount']
        nroomStay = request.form['nroomStay']
        if nroomNo!="":
            content_update = {"$set":{"RoomID":nroomNo}}
            table.update_one(content_find,content_update)        
            data = table.find()
            return render_template("display.html",data=data)
        elif nroomUser!=None and nroomNo==None and nroomCount==None and nroomStay==None:
            content_update = {"$set":{"User":nroomUser}}
            table.update_one(content_find,content_update)
            data = table.find()
            return render_template("display.html",data=data)
        elif nroomCount!=None and nroomNo==None and nroomUser==None and nroomStay==None:
            content_update = {"$set":{"Count":nroomCount}}
            table.update_one(content_find,content_update)
            data = table.find() 
            return render_template("display.html",data=data)
        elif nroomStay!=None and nroomNo==None and nroomUser==None and nroomCount==None:
            content_update = {"$set":{"Stay":nroomStay}}
            table.update_one(content_find,content_update)
            data = table.find()
            return render_template("display.html",data=data)
        elif nroomNo!=None and nroomUser!=None and nroomCount!=None and nroomStay!=None:
            content_update = {"$set":{"RoomID":nroomNo,"User":nroomUser,"Count":nroomCount,"Stay":nroomStay}}
            table.update_one(content_find,content_update)
            data = table.find()
            return render_template("display.html",data=data)
        else:
            flash("No Data Entry")
            return render_template("update.html") 
 
# Display Data In MongoDB          
@app.route("/display-data",methods=['POST','GET'])
def display_data():
    data = table.find()
    return render_template("menu.html")

# To start Flask Application 
if __name__ == '__main__':
    app.run(debug=True,port=5001)
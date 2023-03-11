# Import Statements
from flask import * #Flask to make python program to a web-application 
import pymongo # To connect to MongoDB 
from bson.objectid import ObjectId

# Define Flask app and secret key to show messages in Flask Web
app = Flask(__name__)
app.secret_key="string"

# Initialize MongoDB client
client = pymongo.MongoClient("mongodb+srv://rahulab664:CEZkFDDlOjL253bL@hotel.o79aes9.mongodb.net/?retryWrites=true&w=majority")
db = client["Hotel"]
table = db["Hotel-Room"]
user = db["User"]

#Main Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("login.html")

#Login 
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return render_template("menu.html")
        elif username == "Rahul" and password == "kl.rab_3490":
            return render_template("menu.html")
        else:
            user_find = user.find_one({"username":username,'password':password})
            if user_find:
                return render_template("menu.html")
            else:
                render_template("signup.html")
                flash("Login Failed")
                return render_template("signup.html")

#SignUp
@app.route("/signup",methods=['POST','GET'])
def sign():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_add = {"username":username,'password':password}
        y = user.insert_one(user_add) #Add username and password
        return render_template("menu.html")
    
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
            data =table.find()
            return render_template("display.html",data=data)
        elif choice == "4":
            return render_template("login.html")
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
        room = {
            "RoomID":roomNo,
            "User":roomUser,
            "Count":roomCount,
            "Stay":roomStay
        }
        x = table.insert_one(room)
        data = table.find()
        return render_template("display.html",data=data)

# Removing Data From MongoDB 
@app.route("/remove-data",methods=['POST','GET'])
def remove_data():
    if request.method == 'POST':
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
    else:
        return render_template("menu.html")    
    
# Updating Data In MongoDB
@app.route('/update_data/<room_id>',methods=['GET','POST'])
def update_data(room_id):
    if ObjectId.is_valid(room_id):
        book = table.find_one({'_id':ObjectId(room_id)})
        if request.method == 'POST':
            roomNo = request.form['roomNo']
            roomUser = request.form['roomUser']
            roomCount = request.form['roomCount']
            roomStay = request.form['roomStay']
            table.update_one(
                {'_id':ObjectId(room_id)},
                {'$set':{"RoomID":roomNo,"User":roomUser,"Count":roomCount,"Stay":roomStay}}
            )
            data = table.find()
            return render_template("display.html",data=data)
        else:
            data = table.find()
            flash("No Data Entry")            
            return render_template("update.html",data=data)
    else:
        data = table.find()
        flash("Error")
        return render_template("display.html",data=data) 
 
# Display Data In MongoDB          
@app.route("/display-data",methods=['POST','GET'])
def display_data():
    data = table.find()
    return render_template("menu.html")

# To start Flask Application 
if __name__ == '__main__':
    app.run(debug=True)

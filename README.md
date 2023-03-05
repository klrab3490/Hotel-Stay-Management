# Hotel-Stay-Management

## Copy Git Repository :

- Ubuntu : 
```
sudo apt install git
git clone https://github.com/klrab3490/Hotel-Stay-Management.git
cd Hotel-Stay-Management
```
- Windows : \
  Download [Git Bash](https://git-scm.com/download/win)\
  Download [Git Desktop](https://central.github.com/deployments/desktop/desktop/latest/win32)
```
git clone https://github.com/klrab3490/Hotel-Stay-Management.git
cd Hotel-Stay-Management
```

## Install In Terminal :
```
  pip install pandas
  pip install pymongo
  pip install flask
```
## Install Python :

- [Linux-Python](https://www.python.org/downloads/source/)
- [Windows-Python](https://www.python.org/downloads/windows/)
- [MacOS-Python](https://www.python.org/downloads/macos/)

## Install Mongo DB : 

- [Linux-MongoDB](https://wiki.crowncloud.net/How_To_Install_Duf_On_Ubuntu_22_04?How_to_Install_Latest_MongoDB_on_Ubuntu_22_04)
- [Windows-MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)
- [MacOS-MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

## Flask :

- [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)

## To Run :
```
   cd ~/Hotel-Stay-Management
```
- To run code in Windows : 
```
python app.py
```
- To run code Linus :  
```
python3 app.py 
```

### Current Error :

- Updation is not working
- Hope to recieve on how to clear the update error

## Changes To Make To Run the Code In Your Database :

- Change the client to
```
client = pymongo.MongoClient("mongodb://localhost:27017/")
```
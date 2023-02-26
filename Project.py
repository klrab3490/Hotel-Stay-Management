# Back-end view,insert,update,delete
# eg. Hotel Management

import pymongo
import pandas as pd


class Hotel:
	def __init__(self,n):
		self.client = pymongo.MongoClient("mongodb://localhost:27017/")
		self.db = self.client["Hotel"]
		self.table = self.db["Rooms"]
		while True:
			print("Hotel Management\n 1.Add Room Data\n 2.Remove Room Data\n 3.Update Room Data\n 4.Display Room Data\n 5.Exit")
			a = int(input("   Enter Choice : "))
			if a==1:
				self.add_RoomData()
			elif a==2:
				self.remove_RoomData()
			elif a==3:
				self.update_RoomData()
			elif a==4:
				print("\n")
				self.display_RoomData()
				print("\n")
			elif a==5:
				break
			else:
				print("Invaild Input Try Again")
				b = input ("Do you want to continue?[Y/N]")
				if b=="N" or b=="n":
					print("\n")
					self.display_RoomData()
					print("\n")
					break
	
	def add_RoomData(self):
		roomNo = int(input("Enter The Room Number : "))
		roomUser = input(" Enter Room User Name : ")
		roomCount = int(input("Number Of Prople In The Room : "))
		roomStay = int(input("Enter Days Of Stay : "))
		content_add={"RoomID":roomNo,"User":roomUser,"Count":roomCount,"Stay":roomStay}
		x = self.table.insert_one(content_add)
		print(x.inserted_id)
		print("\n")
		self.display_RoomData()
		print("\n")
			
	def remove_RoomData(self):
		roomNo = int(input("Enter The Room Number : "))
		content_delete = {"RoomID":roomNo}
		data = self.table.find_one(content_delete)
		if data==None :
			print("No data To Delete")
		else :
			print(data)
			self.table.delete_one(data)
			print("data Removed Successfully\n")
			self.display_RoomData()
			print("\n")
			
	def update_RoomData(self):
		roomNo = int(input("Room Data Updation\n Enter Room Number : "))
		content_find = {"RoomID":roomNo}
		data = self.table.find_one(content_find)
		if data==None :
			print("No data To Delete")
		else :
			print(data)
			while True:
				print("What do you want to update? \n 1.Room Number\n 2.User Name \n 3.Count Of People\n 4.Days Of Stay\n 5.All")
				choice = int(input("\t Enter Choice : "))
				if choice==1 :
					nroomNo = int(input("Enter New Room Number : "))
					self.table.update_one({"RoomID":roomNo},{"$set":{"RoomID":nroomNo}})
					break
				elif choice==2 :
					nroomUser = input("Enter New Room User Name : ")
					self.table.update_one({"RoomID":roomNo},{"$set":{"User":nroomUser}})
					break
				elif choice==3 :
					nroomcount = int(input("Enter New User Count : "))
					self.table.update_one({"RoomID":roomNo},{"$set":{"Count":nroomcount}})
					break
				elif choice==4 :
					nroomStay = int(input("Enter the new days of stay : "))
					self.table.update_one({"RoomID":roomNo},{"$set":{"Stay":nroomStay}})
					break
				elif choice==5 :
					nroomNo = int(input("Enter New Room Number : "))
					nroomUser = input("Enter New Room User Name : ")
					nroomcount = int(input("Enter New Count : "))
					nroomStay = int(input("Enter New Days Of Stay : "))
					self.table.update_one({"RoomID":roomNo},{"$set":{"RoomID":nroomNo,"User":nroomUser,"Count":nroomcount,"Stay":nroomStay}})
					break
				else :
					break
			print("\n")
			self.display()
			print("\n")
	
	def display_RoomData(self):
		all_record = self.table.find()
		list_cursor = list(all_record)
		df = pd.DataFrame(list_cursor)
		print(df.head())

print("Assignment 3")
ass = Hotel(0)
print("Exited")
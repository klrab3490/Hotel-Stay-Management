import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Hotel"]
table = db["Hotel-Room"]

for rows in table.find():
    print(rows)
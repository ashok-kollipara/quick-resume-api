import pymongo
import os
import json
import details

# Mongo DB details
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASS = os.getenv('MONGO_PASS')

url = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@resumeapi.qsdmks1.mongodb.net/?retryWrites=true&w=majority"

with pymongo.MongoClient(url) as client:

    db = client.test

    resume_table = db.apicollection

    response = resume_table.find({}, {"_id":0,"basics":1})

    for item in response:
        print(json.dumps(item, indent=4))

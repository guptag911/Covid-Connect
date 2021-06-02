from pymongo import MongoClient
from bson import ObjectId
import json
client = MongoClient('mongodb+srv://dbUser:Abhay.220@cluster0.nhmuu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client.get_database('hackcovid')
users = db.users

# def parse_json(data):
#     return json.loads(json_util.dumps(data))

def get_user(query):
    user = users.find_one(query)
    if user == None:
        return {
            'status': 404
        }
    else:
        return {
            'status': 200,
            'data': user
        }

def insert_user(query):
    user = users.insert_one(query)
    try:
        id = user.inserted_id
        return {
            'status': 200,
            'id': id 
        }
    except Exception as e:
        return {
            'status': 500,
            'error': e
        }
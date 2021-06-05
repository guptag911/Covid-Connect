from pymongo import MongoClient
from bson import ObjectId
import json
import datetime
client = MongoClient('mongodb+srv://dbUser:Abhay.220@cluster0.nhmuu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client.get_database('hackcovid')
posts = db.posts

def addPost(post):
    post['createdAt'] = datetime.datetime.utcnow()
    post['user'] = ObjectId(post['user'])
    newPost = posts.insert_one(post)
    try:
        id = newPost.inserted_id
        return {
            'status': 200,
            'id': id
        }
    except Exception as e:
        return {
            'status': 500,
            'error': "Server Error"
        }
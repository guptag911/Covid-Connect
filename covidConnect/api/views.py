from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404, HttpResponse
from .encryption import getKeyToken, validatePassword

from .usersMongo  import get_user, insert_user
from .postMongo import addPost

from bson import ObjectId, json_util
import json

def parse_json(data):
    return json.loads(json_util.dumps(data))

@api_view(['POST'])
def signup(request):
    if (request.data):
        myUser = request.data
    else:
        myUser = {}

    userQuery = {
        'email': myUser['email']
    }
    user_details = get_user(userQuery)
    if (user_details['status'] == 404):
        # Add this user
        token, key = getKeyToken(myUser['pass'])
        newUser = {
            'name': myUser['name'],
            'address': myUser['address'],
            'zip': myUser['zip'],
            'email': myUser['email'],
            'number': myUser['number'],
            'token': token,
            'key': key
        }
        newUserId = insert_user(newUser)
        return Response(parse_json(newUserId))
    else:
        # User Already Exists
        return Response({
            'status': 500, 
            'error': 'User Already Exists'
        })

@api_view(['POST'])
def signin(request):
    if (request.data):
        myUser = request.data
    else:
        myUser = {}
    
    userQuery = {
        'email': myUser['email']
    }
    user_details = get_user(userQuery)
    if (user_details['status'] == 404):
        return Response({
            'status': 500,
            'error': 'User not found!'
        })
    else:
        user_details = user_details['data']
        if validatePassword(myUser['pass'], user_details['key'], user_details['token']):
            userId = str(user_details['_id'])
            return Response({
                'status': 200,
                'data': userId
            })
        else:
            return Response({
                'status': 500,
                'error': "Wrong User Password!"
            })

@api_view(['POST'])
def user(request):
    if (request.data):
        id = request.data['id']
    else:
        id = ''
    userQuery =  {
        '_id': ObjectId(id)
    }
    userDetails = get_user(userQuery)
    if (userDetails['status'] == 404):
        return Response({
            'status': 500,
            'error': "User Not Found"
        })
    else:
        del userDetails['data']['key']
        del userDetails['data']['token']
        result = {
            'status': 200,
            'data': parse_json(userDetails)
        }
        return Response(result)

@api_view(['POST'])
def post(request):
    data = request.data

    if 'user' not in data:
        return Response({
            'status': 403,
            'error': "Permission Denied"
        })
    
    newPostId = addPost(data)

    return Response(parse_json(newPostId))
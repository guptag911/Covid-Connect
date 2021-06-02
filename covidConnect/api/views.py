from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404, HttpResponse
from .encryption import getKeyToken, validatePassword
from .mongo  import get_user, insert_user
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

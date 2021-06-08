from django.urls import path, include
from .views import myUser, signin, signup, user, addpost, post, UpdateUser

urlpatterns = [
    #Authentication URLS
    path('signup', signup),
    path('signin', signin),

    #User URLS,
    path('user', user),
    path('user/<str:id>', myUser),
    path('update/user', UpdateUser),

    #Posts URLS
    path('posts', addpost),
    path('posts/<int:page>/<str:filter>', post)
]
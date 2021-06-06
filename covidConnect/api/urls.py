from django.urls import path, include
from .views import myUser, signin, signup, user, addpost, post

urlpatterns = [
    #Authentication URLS
    path('signup', signup),
    path('signin', signin),

    #User URLS,
    path('user', user),
    path('user/<str:id>', myUser),

    #Posts URLS
    path('posts', addpost),
    path('posts/<int:page>', post)
]
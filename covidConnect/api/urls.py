from django.urls import path, include
from .views import signin, signup, user, post

urlpatterns = [
    #Authentication URLS
    path('signup', signup),
    path('signin', signin),

    #User URLS,
    path('user', user),

    #Posts URLS
    path('posts', post)
]
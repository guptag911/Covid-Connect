from django.urls import path, include
from .views import signin, signup


urlpatterns = [
    path('signup', signup),
    path('signin', signin)
]
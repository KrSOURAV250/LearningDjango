from django.urls import path
from . import views


urlpatterns = [
    path(route='learn_python', view=views.learn_python, name="learnPython"),
]

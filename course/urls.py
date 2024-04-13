from django.urls import path
from course import views

urlpatterns = [
    path(route="learnpy", view=views.learn_python, name="learnPython"),
    path(route="learndj", view=views.learn_django, name="learnDjango"),
]

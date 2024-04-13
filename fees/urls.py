from django.urls import path
from fees import views

urlpatterns = [
    path(route="pyfee", view=views.python_fees, name="pyfee"),
    path(route="djfee", view=views.django_fees, name="djfee"),
]

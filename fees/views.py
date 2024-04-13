from django.shortcuts import render


# Create your views here.
def python_fees(request):
    return render(request=request, template_name="pythonFee.html")


def django_fees(request):
    return render(request=request, template_name="djangoFee.html")

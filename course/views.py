from django.shortcuts import render
from datetime import datetime


# Create your views here.
def learn_python(request):
    return render(request=request, template_name="laernpy.html")


def learn_django(request):
    context = dict(detail="djanGo iS AwSoMe.", d=datetime.now(), ft=36.987456, names=[
                   "karan", "Ram", "Gautam", "Varun", "Keshav", "Rishav"], student={"stu1": {"name": "sourav", "rollno": 2019374}}, data={"name": "sourav", "rollno": 2019374})
    return render(request=request, template_name="learndj.html", context=context)

from django.shortcuts import render

# Create your views here.
def Jinja_Print(request):
    d={'name':'Subhrajit','age':24,'contact':'9658******'}
    return render(request,'Jinja_Print.html',d)
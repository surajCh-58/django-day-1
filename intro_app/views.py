from django.shortcuts import render

# Create your views here.
def First_intro(request):
    return render(request,'intro_app/index.html')
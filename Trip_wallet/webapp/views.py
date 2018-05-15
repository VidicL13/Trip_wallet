from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, template_name='webapp/login.html')

def signin(request):
    return render(request, template_name='webapp/signin.html')

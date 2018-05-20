from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, template_name='webapp/login.html')

def signin(request):
    return render(request, template_name='webapp/signin.html')

def forgot(request):
    return render(request, template_name='webapp/forgot.html')

def xxx(request):
    return render(request, template_name='webapp/untitled.html')

def newtrip(request):
    return render(request, template_name='webapp/newtrip.html')

def choseTypeUser(request):
    return render(request, template_name='webapp/choseTypeUser.html')

def main(request):
    return render(request, template_name='webapp/main.html')

def addUser(request):
    return render(request, template_name='webapp/addUser.html')

def addDummy(request):
    return render(request, template_name='webapp/addDummy.html')

def addDonator(request):
    return render(request, template_name='webapp/addDonator.html')

def myTrip(request):
    return render(request, 'webapp/myTrip.html', {'title': 'Ime izleta',})

def choseTypeTransaction(request):
    return render(request, template_name='webapp/choseTypeTransaction.html')

def transactionInternal(request):
    return render(request, template_name='webapp/transactionInternal.html')

def transactionDonation(request):
    return render(request, template_name='webapp/transactionDonation.html')

def transactionReceipt(request):
    return render(request, template_name='webapp/transactionReceipt.html')

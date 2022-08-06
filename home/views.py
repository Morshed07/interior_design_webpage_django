from django.shortcuts import render
from home.models import Contact
# Create your views here.

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email= request.POST['email']
        message= request.POST['message']
        contact= Contact(name=name,email=email,message=message)
        contact.save()
    return render(request, 'index.html')
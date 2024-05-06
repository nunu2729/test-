from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name='addis abebast'
    dest1.price=200000000000000
    
    return render(request, 'index.html',{'destination':dest1})
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hai(request):
    return HttpResponse('hai kiran')

def bye(request):
    s= '<h1> love u kiran </h1>'
    return HttpResponse(s)



def frd(request):
    
    return render(request,'sample.html')




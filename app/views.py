from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'joshi','s':{10,20,30,'latha'}}
    return render(request,'looping.html',d)

from django.shortcuts import render
from django.http import HttpResponse
from .models import user_detail_form
from django.http import HttpResponseRedirect
#what is HttpResponse google it.
# Create your views here.

def homepage(request):
    return render(request = request,
                  template_name= 'login_tmp/login.html')
    #return HttpResponse("hey! this is my first django page yay")
def server_chk(response):
    return HttpResponse("<strong> Django Server is running!</strong>")
def wow(response):
    return HttpResponse("wow i am here")
def regist(resopnse):
    return render(resopnse,'login_tmp/Reg.html')

def user_test(request):
    if request.method == 'POST':
        form = user_detail_form(request.POST)  

        if form.is_valid():
        	form.save()
        	return HttpResponseRedirect("register/")
    form = user_detail_form
    return render(request, 'login_tmp/new.html',{'form':form})

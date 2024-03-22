from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')
#def integer(request,pk):
#    data=pk
#    return render(request,'index.html',{'key':data})
#def string(request,pk):
#    data=pk
#    return render(request,'index.html',{'key':data})
#def slug(request,pk):
#    data=pk
#    return render(request,'index.html',{'key':data})
#def path(request,pk):
#    data=pk
#return render(request,'index.html',{'key':data})

def combination(request,pk,id,pkid,idpk):
    data={
        'data1':pk,
        'data2':id,
        'data3':pkid,
        'data4':idpk,
    }
    return render(request,'index.html',{'key':data})


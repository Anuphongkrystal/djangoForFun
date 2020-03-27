from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def hello(request): #เปรียบสเมือนเราสร้าง controler ขึ้นมา
    #return HttpResponse("<h2>Hello World</h2>")

    return render(request,'index.html',{'name':'Onlyone','author':'Levi'})

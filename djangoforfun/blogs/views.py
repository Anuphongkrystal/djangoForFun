from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def hello(request): #เปรียบสเมือนเราสร้าง controler ขึ้นมา
    #return HttpResponse("<h2>Hello World</h2>")
    tags = ['dog','Levi','cat','kookkai']
    rating = 4
    return render(request,'index.html',
    {
    'name':'Onlyone',
    'author':'Levi',
    'tags':tags,
    'rating':rating
    })

def page1(request):
    return render(request,'page1.html')

def createform(request):
    return render(request,'form.html')

def addBlog(request):
    name = request.POST['name']
    desc = request.POST['desc']
    return render(request,'result.html',{'name':name,'desc':desc})

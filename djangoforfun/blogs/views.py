from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User  # สำหรับ register
#from django.http import HttpResponse
# Create your views here.

def hello(request): #เปรียบสเมือนเราสร้าง controler ขึ้นมา

    #quer data
    data = Post.objects.all()
    return render(request,'index.html',{'posts':data})
    #return HttpResponse("<h2>Hello World</h2>")
    '''    tags = ['dog','Levi','cat','kookkai']
        rating = 4
        return render(request,'index.html',
        {
        'name':'Onlyone',
        'author':'Levi',
        'tags':tags,
        'rating':rating
        })
    '''

def page1(request):
    return render(request,'page1.html')

def createform(request):
    return render(request,'form.html')

def addBlog(request):

    username= request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repasssword = request.POST['repassword']

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=firstname,
        last_name=lastname

    )
    user.save()

    return render(request,'result.html')

from django.shortcuts import render,redirect
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

def addUser(request):

    username= request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            print("username ซ้ำกัน")
            return redirect('/createform')
        elif User.objects.filter(email=email).exists():
            print("Email ซ้ำกัน")
            return redirect('/createform')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname

            )
        user.save()
        return redirect('/')
    else:
        return redirect('/createform')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


# READ
def home(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})


# CREATE
def insertData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hifadhi = Student(name=name, email=email, age=age, gender=gender)

        hifadhi.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


# UPDATE
def updateData(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        rekebisha = Student.objects.get(id=id)
        rekebisha.name = name
        rekebisha.email = email
        rekebisha.age = age
        rekebisha.gender = gender
        rekebisha.save()
        return redirect('/')
    else:
        d = Student.objects.get(id=id)
        return render(request, 'edit.html', {'d': d})


# DELETE
def delete(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect('/')


# SIGNUP FILE LOGIC
def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username, password)
        myuser.save()
    return render(request, 'signup.html')


# LOGIN LOGIC
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('username')

        # you have to call data in the db to login so you authenticate my user first

        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'login.html')


# LOGOUT LOGIC
def handlelogout(request):
    logout(request)
    return redirect('/signup')

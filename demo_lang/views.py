from django.shortcuts import render


def signin(req):
    return render(req, 'signin.html')

def signup(req):
    return render(req,'signup.html')

# login required...............................

def home(req):
    return render(req,'index.html')


def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact')
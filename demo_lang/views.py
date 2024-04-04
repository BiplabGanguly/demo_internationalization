from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse


def parse_url(url):
    # Remove leading and trailing slashes and split the URL path by '/'
    url_parts = url.strip('/').split('/')

    if len(url_parts) >= 2:
        language_code = url_parts[0]
        return language_code
    else:
        return None
    
    

def signin(req):
    return render(req, 'signin.html')

def signup(req):
    return render(req,'signup.html')

def varify_user(req):
    if req.method == "POST":
        name = req.POST.get('username')
        password = req.POST.get('pass')
        if name and password:
            user = authenticate(username = name, password = password)
            if user is not None:
                login(req, user)
                return redirect('home')
            return redirect('signin')
        return redirect('signin')    
    return redirect('signin')



# login required...............................

def home(req):
    return render(req,'index.html')


def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')


def change_lang(req):
    if req.method == "POST":
        language = req.POST.get('language')
        print('language..........',language)
        newurl = reverse('home')
        lang_len = len(parse_url(newurl))
        newurl = '/'+language+newurl[lang_len+1:]
        return redirect(newurl)
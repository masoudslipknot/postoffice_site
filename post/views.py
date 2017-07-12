# -*- coding: utf-8 -*-
from connectdb import connect
from django.shortcuts import render , HttpResponseRedirect ,redirect
from .forms import LoginForm
from dataFunc.db import fetch_user
from dataFunc.customerhistory import customerhistory
from dataFunc.getusertype import getusertype


def home(request):
    response = render(request , "home.html", {})
    #response.delete_cookie('loggedIn')
    # response.set_cookie('loggedIn', '1')
    #print request.COOKIES.get('type', None)
    return response

def rahgiri(request):
    if request.method == 'POST':
        url = "/state/"
        id = request.POST['rahgiri']
        url+=id
        print url
        return redirect (url)
    return render(request , "rahgiri.html", {})




def dispatchList(request):
    user = request.COOKIES.get('userID', None)
    if customerhistory(user) != None :
        list =  customerhistory(user)
        context = {"list" : list}
    else:
        context = {"err" : True}
    return render(request , "DispatchList.html", context )



def logout(request):
    print request.COOKIES.get('loggedIn', None)
    response = HttpResponseRedirect ('/')
    response.delete_cookie('loggedIn')
    response.delete_cookie('userID')
    response.delete_cookie('type')
    # response.set_cookie('loggedIn', '1')
    return response

def login(request):
    response = render(request, "login.html", {})
    form = LoginForm(request.POST or None)
    if form.is_valid():
        userID = form.cleaned_data['username']
        password = form.cleaned_data['password']
        con = fetch_user(userID , password)
        type = getusertype(userID)
        response = render(request, "login.html", {})
        if con:
            response = HttpResponseRedirect ('/')
            response.set_cookie('loggedIn', 'True')
            response.set_cookie('userID', userID)
            response.set_cookie('type', type)

            #print request.COOKIES.get('loggedIn', None)
            #print request.COOKIES.get('userID', None)
       # print request.COOKIES.get('loggedIn', None)
        else:
            response = render(request, "login.html", {'err' : True})

    #print request.COOKIES.get('loggedIn', None)

    #response.delete_cookie('loggedIn')
    # response.set_cookie('loggedIn', '1')

    return response


def panel(request):
    print request.COOKIES.get('type', None)
    response = render(request , "panel.html", {})
    #response.delete_cookie('loggedIn')
    # response.set_cookie('loggedIn', '1')
    return response
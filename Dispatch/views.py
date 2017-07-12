# -*- coding: utf-8 -*-
from django.shortcuts import render , HttpResponseRedirect ,redirect
from post.dataFunc.checkstate import rahgiricode
from post.dataFunc.updatestate import seereturneddispatch
def state_case(argument):
    if argument == "مرکز شهر فرستنده":
        print "alireza fuck"
    switcher = {
        "برگشت داده شده": -1,
        "رسیده شده": 2,
        "دفتر پستی فرستنده": 3,
        "مرکز بخش فرستنده": 4,
        "مرکز شهر فرستنده": 5,
        "مرکز استان فرستنده": 6,
        "مرکز استان گیرنده": 7,
        "مرکز شهر گیرنده": 8,
        "مرکز بخش گیرنده": 9,
        "دفتر پستی گرینده": 10
    }
    return switcher.get(argument, "nothing")

def changeState(request ):
    context = {}
    if request.method == 'POST':
        idD = request.POST['idDispatch']
        state = request.POST['sel']
        #idD = str(idD)
        #state = str(state)
        print state
        print idD
        seereturneddispatch(state, idD)
        if seereturneddispatch(state , idD):
            context = {"changed" : True }


    return render(request , "changeState.html", context )


def state_to_string(arg):
    if arg == -1:
        return "برگشت داده شده"
    if arg == 2:
        return "رسیده شده"
    if arg == 3:
        return "دفتر پستی فرستنده"
    if arg == 4:
        return "مرکز بخش فرستنده"
    if arg == 5:
        return "مرکز شهر فرستنده"
    if arg == 6:
        return "مرکز استان فرستنده"
    if arg == 7:
        return "مرکز استان گیرنده"
    if arg == 8:
        return "مرکز شهر گیرنده"
    if arg == 9:
        return "مرکز بخش گیرنده"
    if arg == 10:
        return "دفتر پستی گرینده"
    else:
        return "برگشت داده شده"

def state(request , dispatch_id):
    state_dic = {}
    try:
        state_dic = (rahgiricode(dispatch_id))
        state_dic['state'] = state_to_string(state_dic['state'])
    except:
        state_dic = {"err" : True}
    return render(request , "state.html", state_dic )

def dispatch_indORorg(request):
    return render(request, "make_dispatch/individual_organization.html", {})

def dispatch_org(request):
    return render(request, "make_dispatch/make_dispatch_org.html", {})

def dispatch_ind(request):
    return render(request, "make_dispatch/make_dispatch_ind.html", {})

def makeDispatch(request):
    return render(request, "make_dispatch/make_dispatch_ind.html", {})

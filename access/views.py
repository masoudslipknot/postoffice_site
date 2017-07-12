from django.shortcuts import render
from post.dataFunc.getpostofficename import getpostname
from post.dataFunc.makemanager import makeitmanager
from post.dataFunc.makeworker import makeitworker
from post.dataFunc.Fireemployee import fire
from post.dataFunc.avgtimesender import avgtime
from post.dataFunc.getemployeehistory import getemployerhistory
from post.dataFunc.seereturneddispatch import seereturneddispatch

def setManager(request):
    list = getpostname()
    context = {"list" : list}
    if request.method == 'POST' :
        idU = request.POST['usr']
        postOffice = request.POST['sel1']
        boool = makeitmanager(idU , postOffice)
        if boool:
            context = {"list" : list ,"set" : True}
        if not boool:
            context = {"list" : list , "notSet" : True}
    return render(request , "access/set_manager.html", context )

def setEmployee(request):
    list = getpostname()
    context = {"list": list}
    if request.method == 'POST':
        idU = request.POST['usr']
        postOffice = request.POST['sel1']
        boool = makeitworker(idU, postOffice)
        if boool:
            context = {"list": list, "set": True}
        if not boool:
            context = {"list": list, "notSet": True}
    return render(request , "access/set_employee.html", context )

def fierd(request):
    list = getpostname()
    context = {"list": list}
    if request.method == 'POST':
        idU = request.POST['usr']
        print idU
        boool = fire(idU)
        if boool:
            context = {"list": list, "set": True}
        if not boool:
            context = {"list": list, "notSet": True}
    return render(request , "access/fierd.html", context )

def AVGtime(request):
    return render(request , "AVGtime/avg.html", {} )

def AVGtimeTypeFerestande(request):
    return render(request , "AVGtime/avg.html", {} )




def employeeHistory(request):
    context = {}
    return render(request, "access/employee_history.html", context)

def employeeHistoryList(request):
    context = {}
    if request.method == 'POST':
        idU = request.POST['usr']
        try:
            dic = getemployerhistory(idU)
            context = {"list" : dic}
        except:
            context = {"err": True}
    return render(request, "access/employee_history_list.html", context)


def returnDispatch(request):
    context = {}
    print seereturneddispatch()
    dic = seereturneddispatch()
    context = {"list" : dic}

    return render(request, "access/return-dispatch.html", context)

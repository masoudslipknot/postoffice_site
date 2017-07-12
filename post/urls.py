"""post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import home , login , logout , panel , rahgiri , dispatchList
from Dispatch.views import state , changeState , dispatch_indORorg , dispatch_org , dispatch_ind , makeDispatch
from access.views import setManager , setEmployee , fierd , AVGtime , AVGtimeTypeFerestande , employeeHistory , employeeHistoryList , returnDispatch
urlpatterns = [

    url(r'^make-dispatch/', makeDispatch, name='makeDispatch'),


    url(r'^$', home, name='home'),
    url(r'^login/', login , name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^panel/rahgiri', rahgiri, name='rahgiri'),
    url(r'^panel/dispatchs', dispatchList, name='dispatchList'),
    url(r'^panel/', panel, name='panel'),

    url(r'^make-dispatch/individual', dispatch_ind, name='dispatch_ind'),
    url(r'^make-dispatch/organization', dispatch_org, name='dispatch_Rorg'),
    url(r'^make-dispatch/', dispatch_indORorg, name='dispatch_indORorg'),


    url(r'^set-manager/', setManager, name='set_manager'),
    url(r'^set-employee/', setEmployee , name='set_employee'),
    url(r'^fired/', fierd, name='fierd'),
    url(r'^employee-history/show/', employeeHistoryList, name='employeeHistoryList'),
    url(r'^employee-history/', employeeHistory, name='employeeHistory'),
    url(r'^return-dispatch/', returnDispatch, name='returnDispatch'),


    url(r'^avg-time/type-ferestande', AVGtimeTypeFerestande, name='AVGtime'),
    url(r'^avg-time/type', AVGtime, name='AVGtime'),
    url(r'^avg-time/ferestande', AVGtime, name='AVGtime'),
    url(r'^avg-time/girande', AVGtime, name='AVGtime'),
    url(r'^avg-time/', AVGtime, name='AVGtime'),




    url(r'^state/(?P<dispatch_id>[\w-]+)/$', state , name='state'),
    url(r'^changeState/$', changeState, name='changeState'),
    url(r'^admin/', include(admin.site.urls)),
]

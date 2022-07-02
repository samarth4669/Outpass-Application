from . import views
from django.urls import re_path


urlpatterns = [
    #re_path(r'^home/$',views.home,name='home'),
    re_path(r'^admpanel/$',views.adminhome,name='adminhome'),
    re_path(r'^admdata/$',views.dataentry,name='data'),
    re_path(r'^admdatainfo/$',views.datainfo,name='datainfo'),
    re_path(r'^admdel/(?P<pk>\d+)/$',views.deleting,name="delete"),
    re_path(r'^admedit/(?P<pk>\d+)/$',views.edit,name="edit"),
    re_path(r'^registering/$',views.userregistering,name='winning'), 
    re_path(r'^$',views.userlogin,name='login'), 
    re_path(r'^home/$',views.home,name='home'),
    re_path(r'^loggingout/$',views.userloggingout,name='loggingout'),
    re_path(r'^changing/$',views.changingpassword,name='changing'),
    re_path(r'^bethechange/$',views.plussing,name='plus'),
    re_path(r'^outpass/$',views.outpass,name='outpass'),
    re_path(r'^admpending/$',views.showpending,name='pending'),
    re_path(r'^admfacultyaccept/(?P<pk>\d+)/$',views.facultyaccept,name='facultyaccept'),
    re_path(r'^admfacultydecline/(?P<pk>\d+)/$',views.facultydecline,name='facultydecline'),
    re_path(r'^admfacultyaccep/$',views.showfacultyaccept,name='showfacultyaccept'),
    re_path(r'^admfacultydec/$',views.showfacultydecline,name='showfacultydecline'),

]
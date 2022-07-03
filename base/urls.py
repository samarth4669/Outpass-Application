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
    re_path(r'^admspecialwarden/$',views.specialrequestforwarden,name='specialwarden'),
    re_path(r'^admwardenaccept/(?P<pk>\d+)/$',views.acceptwarden,name='acceptwarden'),
    re_path(r'^admwardendecline/(?P<pk>\d+)/$',views.wardendecline,name='declinewarden'),
    re_path(r'^admspecialcoordinate/$',views.specialrequestforcoordinater,name='specialcoordinater'),
    re_path(r'^admcoordaccept/(?P<pk>\d+)/$',views.acceptcoordinate,name='acceptcoordinater'),
    re_path(r'^admcoorddecline/(?P<pk>\d+)/$',views.declinecoordinate,name='declinecoordinater'),
    re_path(r'^studentpending/$',views.studentpending,name='studentpending'),
    re_path(r'^studentaccept/$',views.studentaccepted,name='studentaccept'),
    re_path(r'^studentdecline/$',views.studentdeclined,name='studentdecline'),
    re_path(r'^message/$',views.message,name='message'),
    re_path(r'^admmessage/$',views.messageinfaculty,name='messageinfaculty'),
     re_path(r'^admanswering/(?P<pk>\d+)/$',views.answerthequery,name='answerthequery'),
    re_path(r'^admdelty/(?P<pk>\d+)/$',views.contact_del,name='dealt'),
    re_path(r'^getpass/$',views.getoutpassemail,name='getoutpass'),
    
    
    
    

]
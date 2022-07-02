from errno import EMLINK
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from .models import data
import smtplib as s
from django.contrib.auth.models import User,Group,Permission
from email.message import EmailMessage as e
import random
import string
from manager.models import requesting
import datetime

# Create your views here.
global perm
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    q=request.user
    s=data.objects.get(studentid=q).facultyname  
    o=data.objects.get(studentid=q).Name  
    print(request.user,"ddd")    
    
    

    
       
    return render(request,'front/home.html',{'object':s,'o':o})
def adminhome(request):
    perm=0
    for i in request.user.groups.all():
                if i.name=="masteruser":
                        perm=1
    if not request.user.is_authenticated and perm!=1:
        return redirect('login')
    return render(request,'back/panel.html')
def dataentry(request):
    # to check if user is logged in or not
    perm=0
    for i in request.user.groups.all():
                if i.name=="masteruser":
                        perm=1
    if not request.user.is_authenticated and perm!=1:
        return redirect('login')
     
    if request.method=="POST":
       name=request.POST.get('name')
       ide=request.POST.get('studentid')
       faculty=request.POST.get('facultyid')
       facultyname=request.POST.get('facultyname')
       roles=request.POST.getlist('roles')
       

       print(name,ide,faculty,facultyname,roles)
       if name=="" or ide=="" or faculty=="" or facultyname=="" or roles=="":
           error="Please fill all input field as evrything is necessary"
           return render(request,"back/error.html",{'error':error})
       created= data()
       created.Name=name
       created.studentid=ide
       created.facultymailid=faculty
       created.facultyname=facultyname
       
       created.x=roles
       created.save()   
    return render(request,"back/dataentry.html")
def datainfo(request):
    perm=0
    for i in request.user.groups.all():
                if i.name=="masteruser":
                        perm=1
    if not request.user.is_authenticated and perm!=1:
        return redirect('login')
    s=request.user.username    
    dat=data.objects.filter(facultymailid=s)
    return render(request,"back/datainfo.html",{'dat':dat})   
def deleting(request,pk):
    perm=0
    for i in request.user.groups.all():
                if i.name=="masteruser":
                        perm=1
    if not request.user.is_authenticated and perm!=1:
        return redirect('login')
    b=data.objects.filter(pk=pk)
    b.delete()   
    return redirect('datainfo')
def edit(request,pk):
    perm=0
    for i in request.user.groups.all():
                if i.name=="masteruser":
                        perm=1
    if not request.user.is_authenticated and perm!=1:
        return redirect('login')
    editing=data.objects.get(pk=pk)
    if request.method=="POST":
       name=request.POST.get('name')
       ide=request.POST.get('studentid')
       faculty=request.POST.get('facultyid')
       facultyname=request.POST.get('facultyname')
       roles=request.POST.getlist('roles')
       print(roles)
       if name=="" or ide=="" or faculty=="" or facultyname=="" or roles=="":
           error="Please fill all input field as evrything is necessary"
           return render(request,"back/error.html",{'error':error})
       
       editing.Name=name
       editing.studentid=ide
       editing.facultymailid=faculty
       editing.facultyname=facultyname
       
       editing.x=roles
       
       editing.save()

    

    
    return render(request,'back/edit.html',{'pk':pk,'editing':editing })              


       
          
       
        

    
def userregistering(request):
   
    if request.method=="POST":
        name=request.POST.get('name')
        username1=request.POST.get('id')
        passingword1=request.POST.get('password1')
        passingword2=request.POST.get('password2')
        email=request.POST.get('email')
        key=request.POST.get('secret')
        print(key)
        print(name,username1,email)

        if passingword1!=passingword2:
            error="please input same password and verify password"
            return render(request,"front/erroring.html",{'error':error})  

        

        count1=0 
        count2=0 
        count3=0 
        count4=0 
        for i in passingword1:
            if i>='0' and i<='9':
                count1=1   
            if i>='A' and i<='Z':
                count2=1  
            if i>='a' and i<='z':
                count3=1  
            if i in ['!','@','#','$','%','^','&','*','(',')']:
                count4=1
        if count1==0 or count2==0 or count3==0 or count4==0:
            warn="your password is not strong"
            return render(request,"front/erroring.html",{'warn':warn}) 
        if(len(passingword1)<8):
            warn="your password must contain minimum 8 character"
            return render(request,"front/erroring.html",{'warn':warn})
        if(len(User.objects.filter(username=username1))==0) and (len(User.objects.filter(email=email))==0):
            if(key!="xywz"):
                derive=data.objects.filter(studentid=username1)
                if(len(derive)==0):
                    error="you are not registerd into database.please contact your respective faculty advisor."
                    return render(request,"front/erroring.html",{'error':error})
                else: 
                    user=User.objects.create_user(username=username1,email=email,password=passingword1)    
            

            
            
            elif(key=="xywz"):
                user=User.objects.create_user(username=username1,email=email,password=passingword1) 
                g = Group.objects.get(name='masteruser')
                user=User.objects.get(username=username1)
                g.user_set.add(user)
                print(g)
             
            w=email
            print(w)
            email=e()
        
            email['from']='21BCS110'
            email['to']=w
            email['subject']='registering  into account'
            email.set_content("congrats!you are registerd now!! ")
            with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                       smtp.ehlo()
                       smtp.starttls()
                       smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                       smtp.send_message(email)  
           
            


    return render(request,'front/userslogin.html')     


def userlogin(request):
    
    if request.method=="POST":
        username1=request.POST.get('id')
        passingword=request.POST.get('password')
        
        
        
        
        if username1!="" and passingword!="":
            user=authenticate(username=username1,password=passingword)
            #if user doesnot exist then none is return and if it exist its information stores in that variable user  
            if user!=None:
                login(request,user)#login request for that user
                perm=0
                for i in request.user.groups.all():
                       if i.name=="masteruser":
                                 perm=1
                print(perm)                 
                if(perm==1):

                      w=request.user.email 
                      print(w)
                      email=e()
        
                      email['from']='21BCS110'
                      email['to']=w
                      email['subject']='logging into account'
                      email.set_content("you are logged into your account")
                      with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                             smtp.ehlo()
                             smtp.starttls()
                             smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                             smtp.send_message(email)
                      return redirect('adminhome')
                else:
                      w=request.user.email 
                      print(w)
                      email=e()
        
                      email['from']='21BCS110'
                      email['to']=w
                      email['subject']='logging into account'
                      email.set_content("you are logged into your account")
                      with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                             smtp.ehlo()
                             smtp.starttls()
                             smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                             smtp.send_message(email)
                      return redirect('home')

            else:
                error="Please fill valid user and password"
                return render(request,"front/erroring.html",{'error':error})  


        elif  username1=="" or passingword=="": 
            error="Please fill all input field as evrything is necessary"
            return render(request,"front/erroring.html",{'error':error})      
            


    return render(request,'front/userslogin.html')    
    
def userloggingout(request):
    logout(request)

    return redirect('login')    

def changingpassword(request):
    N = 5
  
 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    print(res)
    global mini
    mini=res   
    if request.method=="POST":
        global email1
        email1=request.POST.get('reminder-email')
        print(email1)
        email=e()
        
        email['from']='21BCS110'
        email['to']=email1
        email['subject']='changing the password'
        email.set_content(mini)
        with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                 smtp.ehlo()
                 smtp.starttls()
                 smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                 smtp.send_message(email)
    return render(request,'front/plussing.html')  



def plussing(request):
    if request.method=="POST":
        verify1=request.POST.get('verify')
        newpass=request.POST.get('set')
        print(verify1,newpass,mini)
        if verify1!=mini:
            warn="enter correct verifying pass"
            return render(request,"front/erroring.html",{'error':warn}) 
        count1=0 
        count2=0 
        count3=0 
        count4=0 
        for i in newpass:
            if i>='0' and i<='9':
                count1=1   
            if i>='A' and i<='Z':
                count2=1  
            if i>='a' and i<='z':
                count3=1  
            if i in ['!','@','#','$','%','^','&','*','(',')']:
                count4=1
        if count1==0 or count2==0 or count3==0 or count4==0:
            warn="your password is not strong"
            return render(request,"front/erroring.html",{'error':warn}) 
        if(len(newpass)<8):
            warn="your password must contain minimum 8 character"
            return render(request,"front/erroring.html",{'error':warn}) 
        a=User.objects.get(email=email1)
        print(a)
        a.set_password(newpass)
        a.save()
        return redirect('login')  
    return render(request,'front/bethechange.html')      


def outpass(request):
    q=request.user
    o=data.objects.get(studentid=q).Name
    fac=data.objects.get(studentid=q).facultyname
 
    if request.method=="POST":
        reason=request.POST.get('reason')
        email=request.POST.get('email')
        
        
        days=request.POST.get('days')
        t1=request.POST.get('starttime')
        t2=request.POST.get('endtime')
        d1=request.POST.get('leaving')
        d2=request.POST.get('returning')
        
        print(fac,reason,email,days,t1,t2,d1,d2)
        if(d1>d2):
            error="please choose correct startdate and enddate"
            return render(request,"front/erroring.html",{'error':error})
        if(d1==d2 and t1>t2):
            error="please choose correct startdate and enddate"
            return render(request,"front/erroring.html",{'error':error})
        dto1= datetime.datetime.strptime(d1, '%Y-%m-%d').date()    
        dto2= datetime.datetime.strptime(d2, '%Y-%m-%d').date() 
        print(type(dto1))
        tto1=datetime.datetime.strptime(t1,'%H:%M').time()
        tto2=datetime.datetime.strptime(t2,'%H:%M').time()
        print(tto1)
        dt1=datetime.datetime.combine(dto1,tto1)
        dt2=datetime.datetime.combine(dto2,tto2)
        print(dt1)
        current=datetime.datetime.now()        
        print(current) 
        print(dt1>dt2)
        requestingobj=requesting()
        requestingobj.reason=reason
        requestingobj.days=days
        requestingobj.email=email 
        requestingobj.starttime=dt1
        requestingobj.endtime=dt2
        requestingobj.faculty=fac
        requestingobj.save()
        faculty=data.objects.get(studentid=q).facultymailid
        we=User.objects.get(username=faculty).email



                 
            







       
        email=e()
        
        email['from']='21BCS110'
        email['to']=we
        email['subject']='new request has been updated'
        email.set_content("pending request")
        with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                       smtp.ehlo()
                       smtp.starttls()
                       smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                       smtp.send_message(email)      
                      
        


    




         

 
    return render(request,'front/outpass.html',{'o':o,})
def showpending(request):
    q=request.user
    x=data.objects.filter(facultymailid=q)
    o=x[0].facultyname

    pendingobj=requesting.objects.filter(faculty=o).filter(status="pending").filter(isfaculty="no")
    return render(request,'back/pending.html',{'pendingobj':pendingobj})   
def facultyaccept(request,pk):
    acceptobj=requesting.objects.get(pk=pk)
    if(acceptobj.days<=10):
        acceptobj.isfaculty="yes"
        acceptobj.iswarden="yes"
        acceptobj.islifecoordinator="yes"
        acceptobj.status="accepted"
        w=acceptobj.email
        acceptobj.save()
        email=e()
        
        email['from']='21BCS110'
        email['to']=w
        email['subject']='accepting the request'
        email.set_content("your request for levave has been accepted ")
        with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                            smtp.send_message(email) 
        return redirect('pending')  
    else:
        acceptobj.isfaculty="yes"
        acceptobj.save()
        email=e()
        q=data.objects.all()
        for i in q:
            if "Warden" in i.x:
                g=i
                break
        for i in q:
            if "Student-life coordinator" in i.x:
                k=i
                break    
        wardenemail=User.objects.get(username=g.facultyid).email
        coordinator=User.objects.get(username=k.facultyid).email
        email['from']='21BCS110'
        email['to']=wardenemail,coordinator
        email['subject']='new request '
        email.set_content("new request has been updated")
        with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                            smtp.send_message(email) 
        return redirect('pending')  

def facultydecline(request,pk):
    decliningobj=requesting.objects.get(pk=pk)
    decliningobj.status="declined"
    w=decliningobj.email
    decliningobj.save()
    email=e()
        
    email['from']='21BCS110'
    email['to']=w
    email['subject']='declining the request'
    email.set_content("your request for levave has been declined by your faculty advisor ")
    with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login('21bcs110@iiitdwd.ac.in','cqidtruxzsxarlfn')
                            smtp.send_message(email) 
    return redirect('pending')
def showfacultyaccept(request):
    q=request.user
    x=data.objects.filter(facultymailid=q)
    o=x[0].facultyname
    query=requesting.objects.filter(faculty=o).filter(isfaculty="yes")
    return render(request,'back/facultyaccept.html',{'query':query})
def showfacultydecline(request):
    q=request.user
    x=data.objects.filter(facultymailid=q)
    o=x[0].facultyname
    query=requesting.objects.filter(faculty=o).filter(status="declined").filter(isfaculty="no")
    return render(request,'back/facultydecline.html',{'query':query})    





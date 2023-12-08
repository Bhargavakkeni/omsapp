from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginDetails,OmsAdmin
from django.template import loader,Context
from django.views.decorators.csrf import csrf_protect
# Create your views here.

#global name to associate user with records and login
#adminName=''

#for notifying starting of server
def root(request):
    return HttpResponse('Server has started')

@csrf_protect
#for displaying login page
def index(request):
    #template = loader.get_template('loginapp/index.html')
    return render(request,'loginapp/index.html')

#for verifying the user login details
@csrf_protect
def verifyUser(request):
    #global adminName
    mydict={}
    username=request.POST['userName']
    password=request.POST['password']
    #print(type(username))
    username=username.strip()
    #print(username,len(username))
    verifyname,verifypassword='',''
    verify= LoginDetails.objects.filter(username=username,password=password).values() #fetch the data from the table which matches the username
    #details=LoginDetails.objects.all().values()
    #print(details,username)
    for x in verify:
        if username == x['username']:
            verifyname = x['username']
            verifypassword = x['password']
    #if verified notifies the user with successful msg
    if username==verifyname and password==verifypassword:
        mydict={
            'verify':True,
            'error':False,
            'name':username,
            #'adminName':username,
        }
        #adminName=username
        #print(adminName)
    else:
        mydict['error']=True
    #template = loader.get_template('loginapp/index.html') 
    #return HttpResponse(template.render(mydict,request))
    return render(request,'loginapp/index.html',context=mydict)

#to go to password reset page
def resetpass(request):
    template=loader.get_template('loginapp/forgotpassword.html')
    return HttpResponse(template.render())


#for password change
def changepass(request):
    template=loader.get_template('loginapp/forgotpassword.html')
    username=request.GET['userName']
    username=username.strip()
    newpassword=request.GET['newpassword']
    password='password'
    details=LoginDetails.objects.filter(username=username).values()
    print(details)
    mydict={
        'passverify':False,
        'passerror':False,
    }
    #if user exist
    if details:
        mydict['passverify']=True
        kargs={password:newpassword}
        LoginDetails.objects.filter(username=username).update(**kargs)
    else:
        mydict['passerror']=True    
    return HttpResponse(template.render(mydict,request))

#for logging out
def logout(request,adminName=''):
    #global adminName
    template = loader.get_template('loginapp/OmsAdmin1.html')
    adminName=''
    mydict={
        'adminName':adminName,
    }
    return HttpResponse(template.render(mydict,request))

#for registration page
def registration(request):
    template = loader.get_template('loginapp/registration.html')
    return HttpResponse(template.render())

#for uplading new user login data to the model
def uploading(request):
    username=request.GET['userName']
    password=request.GET['password']
    username=username.strip()
    mydict={}
    details=LoginDetails.objects.filter(username=username).values()
    #print(details,username)
    mydict={
        'verify':False,
        'error':False
    }
    #check whether user already exist or not
    for x in details:
        if username == x['username']:
            mydict['error']=True  
    #if user doesn't exist create a record and save it
    if(mydict['error']==False):
        mydict['verify']=True
        myobj = LoginDetails(username=username, password=password)
        myobj.save()
    template=loader.get_template('loginapp/registration.html')
    return HttpResponse(template.render(mydict,request))

#for displaying a CRUD omsadmin page when login is successful
def omsadmin(request,adminName=''):
    template=loader.get_template('loginapp/OmsAdmin1.html')
    if adminName=='admin':
        details=OmsAdmin.objects.all().values()
    else:
        details=OmsAdmin.objects.filter(username_id=adminName).values()
    #print(details)
    mydict={
        'mydetails':details,
        'adminName':adminName
    }
    return HttpResponse(template.render(mydict,request))

#to show all the records associated with username
def show(request,adminName=''):
    if adminName=='admin':
        details=OmsAdmin.objects.all().values()
    else:
        details=OmsAdmin.objects.filter(username_id=adminName).values()
    #print(details)
    mydict={
        'verify':True,
        'mydetails':details,
        'adminName':adminName,
    }
    template=loader.get_template('loginapp/OmsAdmin1.html')
    return HttpResponse(template.render(mydict,request))

#to add new records to the omsadmin corresponding to the username
def add(request,adminName=''):
    if adminName=='admin':
        details=OmsAdmin.objects.all().values()
    else:
        details=OmsAdmin.objects.filter(username_id=adminName).values()
    brand=request.GET['brand']
    shipMethod=request.GET['shipMethod']
    processingDays=request.GET['processingDays']
    processingDaysType=request.GET['processingDaysType']
    min=request.GET['min']
    max=request.GET['max']
    processingDate=request.GET['processingDate']
    availableToPromiseDate=request.GET['availableToPromiseDate']
    cutOff=request.GET['cutOff']
    obj=OmsAdmin(brand=brand,shipMethod=shipMethod,processingDays=processingDays,processingDaysType=processingDaysType,min=min,max=max,processingDate=processingDate,availableToPromiseDate=availableToPromiseDate,cutOff=cutOff,username_id=adminName)
    obj.save()
    mydict={
        'addverify':True,
        'adminName':adminName,
        'mydetails':details,
    }
    template=loader.get_template('loginapp/OmsAdmin1.html')
    return HttpResponse(template.render(mydict,request))

#to update individual specified fields in the omsadmin
def update(request,adminName=''):
    mydict={}
    if adminName=='admin':
        details=OmsAdmin.objects.all().values()
    else:
        details=OmsAdmin.objects.filter(username_id=adminName).values()
    template=loader.get_template('loginapp/OmsAdmin1.html')
    idUpdate=request.GET['idUpdate']
    if idUpdate=='None':
        mydict={
            'updateerror':True,
            'mydetails':details,
            'adminName':adminName,
        }
        return HttpResponse(template.render(mydict,request))
    else:
        fieldUpdate=request.GET['fieldUpdate']
        newValue=request.GET['newValue']
        kargs={fieldUpdate:newValue} #a dictionary to hold to be updated values
        OmsAdmin.objects.filter(id=idUpdate).update(**kargs) #to send variable length key value arguments
        mydict={
            'updateverify':True,
            'mydetails':details,
            'adminName':adminName,
        }
        return HttpResponse(template.render(mydict,request))

#to delete specified records from omsadmin
def delete(request,adminName=''):
    template=loader.get_template('loginapp/OmsAdmin1.html')
    if adminName=='admin':
        details=OmsAdmin.objects.all().values()
    else:
        details=OmsAdmin.objects.filter(username_id=adminName).values()
    idDelete=request.GET['idDelete']
    if idDelete=='None':    
        mydict={
            'deleteerror':True,
            'mydetails':details,
            'adminName':adminName,
        }
        return HttpResponse(template.render(mydict,request))
    else:
        OmsAdmin.objects.filter(id=idDelete).delete() 
        mydict={
            'deleteverify':True,
            'mydetails':details,
            'adminName':adminName,
        }
        return HttpResponse(template.render(mydict,request))

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template=loader.get_template('calculatorapp/index.html')
    return HttpResponse(template.render())

def submitquery(request):
    template = loader.get_template('calculatorapp/index.html')
    q=request.GET['query']
    try:
        ans=eval(q)
        mydict={
            'q':q,
            'ans':ans,
            'error':False,
            'result':True 
        }
        return HttpResponse(template.render(mydict,request)) #render(request,'index.html',context=mydict)
    except:
        mydict={
            'error':True,
            'result':False
        }
        return HttpResponse(template.render(mydict,request)) #render(request,'index.html',context=mydict)

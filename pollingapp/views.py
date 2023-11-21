from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
# Create your views here.
arr=['C','Python','Java','Kotlin','C++','Ruby','Javascript','PHP','.net','swift','MySQL','HTML','Odoo']
globaldictcnt=dict()
def index(request):
    template =loader.get_template('pollingapp/index.html')
    mydict={
        'arr': arr
    }
    return  HttpResponse(template.render(mydict,request)) #render(request,"index.html",context=mydict)

def getquery(request):
    template = loader.get_template('pollingapp/index.html')
    q=request.GET['languages']
    if q in globaldictcnt:
        globaldictcnt[q]=globaldictcnt[q]+1
    else:
        globaldictcnt[q]=1
    mydict={
            'arr':arr,
            'globaldictcnt':globaldictcnt
        }
    return HttpResponse(template.render(mydict,request)) #render(request,'index.html',context=mydict)

def sortdata(request):
    global globaldictcnt
    globaldictcnt=dict(sorted(globaldictcnt.items(),key=lambda x:x[1],reverse=True))
    template=loader.get_template('pollingapp/index.html')
    mydict={
        'arr':arr,
        'globaldictcnt':globaldictcnt
    }
    return HttpResponse(template.render(mydict,request)) #render(request,'index.html',context=mydict)
from django.shortcuts import render
from whatever.models import Whatever
from django.template.context_processors import csrf
from django.utils import timezone
from whatever.forms import WhateverForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def whatever(request):
    args ={}
    args.update(csrf(request))
    args['whatever']=Whatever.objects.all()
    #print (args)
    #.{'csrf_token': <SimpleLazyObject: <function csrf.<locals>._get_val at 0x0000015AA0C9D0D8>>, 'whatever': <QuerySet [<Whatever: Whatever object (1)>]>}

    return render(request,'index.html',args)

def add(request):
    if request.POST:
        form=WhateverForm(request.data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=WhateverForm()
        args={}
        args.update(csrf(request))
        args['form']=form
       # return render(request,'add.html',{'form':form})
        return render(request,'add.html',args)
    
# This is where your views go :)
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView
#from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render_to_response

import md5
import datetime
from jarvis.models import CodeShare

def store_code(request, parent_md5=None):
    if request.method == "POST":
        parent = None
        if 'parent' in request.POST:
            parent = get_object_or_404(CodeShare, md5=request.POST['parent'])
        cs = CodeShare(md5=md5.new(request.META.REMOTE_ADDR+repr(datetime.datetime.now())).hexdigest(),
                       code=request.POST['code'], parent=parent)
        cs.save()
        return redirect('jarvis-code', md5=cs.md5)
    else:
        return render_to_response('jarvis/jarvis.html', {'parent_md5': parent_md5})

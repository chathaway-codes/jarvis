# This is where your views go :)
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView
#from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

import md5
import datetime
from jarvis.models import CodeShare

def store_code(request, parent_md5=None):
    if request.method == "POST":
        parent = None
        if parent_md5 != None:
            parent = get_object_or_404(CodeShare, md5=parent_md5)
        my_md5 = md5.new(request.META['REMOTE_ADDR']+repr(datetime.datetime.now())).hexdigest()
        i = 10
        while CodeShare.objects.filter(md5=my_md5[:i]).count() > 0 and i < 32:
            i += 1
        cs = CodeShare(md5=my_md5[:i],
                       code=request.POST['code'], parent=parent)
        cs.save()
        return redirect('jarvis-code', parent_md5=cs.md5)
    else:
        if parent_md5 != None:
            parent = get_object_or_404(CodeShare, md5=parent_md5)
            return render_to_response('jarvis/jarvis.html', RequestContext(request, {'parent_md5': parent_md5, 'code': parent.code,
                'url': request.build_absolute_uri(reverse('jarvis-code', kwargs={'parent_md5': parent_md5}))}))
        return render_to_response('jarvis/jarvis.html', RequestContext(request, {'parent_md5': parent_md5}))

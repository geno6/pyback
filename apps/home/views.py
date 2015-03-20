from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from .tasks import home_task

class HomeView(View):
    def get(self, request):
        home_task.delay()
        return render_to_response('home/index.html', context_instance=RequestContext(request))
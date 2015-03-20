from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render_to_response('home/index.html', context_instance=RequestContext(request))
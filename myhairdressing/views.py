from django.shortcuts import render
from .models import Hairdressing,Citation,Schedule
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.

def mainpage(request):
    template = get_template("index.html")
    variables = Context({
        'user' : request.user
    })
    output = template.render(variables)
    return HttpResponse(output)

class HairdressingDetail(DetailView):
    model = Hairdressing
    template_name = 'hairdressing-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(HairdressingDetail, self).get_context_data(**kwargs)
        return context


class Citations(DetailView):
    model = Citation
    template_name = 'citations.html'

    def get_context_data(self, **kwargs):
        context = super(Citations,self).get_context_data(**kwargs)
        return context

def CreateCitation(request):
    u = request.POST.get('user')
    us = User.objects.get(username=u)
    s = request.POST.get('schedule')
    sc = Schedule.objects.get(pk=s)

    c = Citation(id_user=us, id_schedule=sc)
    c.save()
    return redirect('/citations?a=1')

def DeleteCitation(request):
    id_citation = request.POST.get('id_citation')
    citation = Citation.objects.get(id=id_citation)
    citation.delete()
    return redirect('/citations')
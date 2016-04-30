from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from myhairdressing.models import Hairdressing,Citation,Schedule
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from myhairdressing.forms import *

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
    if (u == 'AnonymousUser'):
        return redirect('/login?id=1')
    else:
        us = User.objects.get(username=u)

        s = request.POST.get('schedule')
        sc = Schedule.objects.get(pk=s)

        c = Citation(id_user=us, id_schedule=sc)
        c.save()
        return redirect('/citations')


def DeleteCitation(request):
    id_citation = request.POST.get('id_citation')
    citation = Citation.objects.get(id=id_citation)
    citation.delete()
    return redirect('/citations')


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = Hairdressing(filename = request.POST['filename'],docfile = request.FILES['imgfile'])
            newimg.save(form)
            return redirect("uploads")


"""def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request,'registration/register.html', context)
"""

def register(request):
    if request.method == 'POST':

        form = RegisterUserForm(request.POST, request.FILES)

        if form.is_valid():

            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)

            user_model.email = email

            user_model.save()

            return redirect(reverse('registration.thanks', kwargs={'username': username}))
    else:

        form = RegisterUserForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def thanks_view(request, username):
    return render(request, 'registration/thanks.html', {'username': username})
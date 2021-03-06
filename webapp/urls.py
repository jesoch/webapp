from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.http import request
from myhairdressing.forms import UploadForm,RegisterUserForm
from myhairdressing import views
from myhairdressing.views import *
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage, name='Home'),
    url(r'^login/$', 'django.contrib.auth.views.login', kwargs={'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}),
    url(r'^register/$', views.register, name='registre'),
    url(r'^citation/create/$', views.CreateCitation, name='citation_create'),
    url(r'^citation/delete/$', views.DeleteCitation, name='citation_delete'),

    # Hairdressings

    url(r'^hairdressing/$',
        ListView.as_view(
            queryset=Hairdressing.objects.all(),
            context_object_name='HairdressingList',
            template_name='hairdressinglist.html'),
        name='hairdressingList'),

    # Hairdressing details
    url(r'^hairdressing/(?P<pk>\d+)/$',
        HairdressingDetail.as_view(),
        name='hairdressing_detail'),

    # User Citation
    url(r'^citations/$',
        ListView.as_view(
            queryset=Citation.objects.all(),
            context_object_name='CitationsList',
            template_name='citations.html', ),
        name='Citations'),

    url(
        r'thanks/(?P<username>[\w]+)/$',
        views.thanks_view,
        name='registration.thanks'
    ),
)

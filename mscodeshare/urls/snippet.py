from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from codeshare.models import  snippet
from django.conf.urls import include, url


snippet_info= {'query': snippet.objects.all()}
urlpatterns = patterns('',
                       url(r'^$',object_list, dict(snippet_info, paginate_by=20),
                           name='snippet_info'),
                       url(r'^(?P<object_id>\d+)/$',object_detail, snippet_info,
                           name="snippet_details"),
                       )

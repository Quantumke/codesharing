from django.views.generic.list import  ListView
from django.views.generic.detail import DetailView
from codeshare.models import  snippet
from django.conf.urls import include, url
from django.conf.urls import patterns, include, url
# from django.views.generic.list import object_list, object_detail
# from django.views.generic.detail import object_list, object_detail


snippet_info= {'query': snippet.objects.all()}
urlpatterns = patterns('',
                       url(r'^$',ListView.as_view(), dict(snippet_info, paginate_by=20),
                           name='snippet_info'),
                       url(r'^(?P<object_id>\d+)/$',DetailView.as_view(), snippet_info,
                           name='snippet_details'),
                       )

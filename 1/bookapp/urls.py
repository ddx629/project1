
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'book/create/$', create_book),
    (r'book/list/$', list_book ),
    (r'book/edit/(?P<id>[^/]+)/$', edit_book),
    (r'book/view/(?P<id>[^/]+)/$', view_book),
    (r'book/delete/(?P<id>[^/]+)/$', delete_book),
##    (r'book/search-form/$', search_form),                   
    (r'book/search/$', search),
                       
    (r'author/create/$', create_author),
)

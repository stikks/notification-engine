__author__ = 'stikks'
# import core django logic
from django.conf.urls import url

# import third party extensions
from rest_framework.urlpatterns import format_suffix_patterns

# import application logic
import views

urlpatterns = [
    url(r'^applications/$', views.ClientApplicationList.as_view(), name="app-list"),
    url(r'^applications/(?P<pk>[0-9]+)/$', views.ClientApplicationDetail.as_view(), name="app-detail"),
    url(r'^messages/$', views.SendDownstreamHTTP.as_view(), name="send-message"),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
    url(r'^$', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)
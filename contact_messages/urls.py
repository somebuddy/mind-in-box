from django.conf.urls import url, patterns
from .views import MessageCreateView, MessageListView

urlpatterns = patterns(
    '',
    url(r'^add/$', MessageCreateView.as_view(), name='add'),
    url(r'^$', MessageListView.as_view(), name='list'),
)

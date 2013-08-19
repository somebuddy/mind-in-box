from django.conf.urls import url, patterns
from django.views.generic import TemplateView
from .views import BitstarterView

urlpatterns = patterns(
    '',
    url(r'^$', BitstarterView.as_view(), name='home'),
)

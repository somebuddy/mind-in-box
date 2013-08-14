from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('bitstarter.urls', namespace='bitstarter')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cb/balance', 'coinbase.views.balance'),
    url(r'^cb/orders', 'coinbase.views.orders'),
    url(r'^cb/sell', 'coinbase.views.sell'),

)

urlpatterns += patterns(
    '',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

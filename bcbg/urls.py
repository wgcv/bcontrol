from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bcbg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'personal.views.home', name='home'),
    url(r'^agregarBombero/', 'personal.views.agregarBombero', name='agregarBombero'),
    url(r'^perfil/(?P<d>\w+)/$', 'personal.views.perfil', name='perfil'),
    url(r'^admin/', include(admin.site.urls)),
)

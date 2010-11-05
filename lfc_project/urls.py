# python imports
import os

# django imports
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template

admin.autodiscover()
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfc.views.fiveohoh'

# Django 
urlpatterns = patterns('',
    url('^accounts/login/?$', login, {"template_name" : "admin/login.html"}, name='auth_login'),
    url('^accounts/logout/?$', logout, name='auth_logout'),

    (r'^admin/(.*)', admin.site.root),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('django.conf') }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)

# LFC Blog
urlpatterns += patterns("",
    (r'', include('lfc_blog.urls')),
)

# LFC
urlpatterns += patterns('',
    (r'^manage/', include('lfc.manage.urls')),
    (r'', include('lfc.urls')),
)
from django.conf.urls.defaults import *
from django.conf import settings

# the chart data views
urlpatterns = patterns('demoapp.views',
    ('^data/$','chart_data'),
    ('^bar_chart','bar_chart'),
	('^insert', 'insert')
)
# the front page
urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
)  
                
# serve static content
baseurlregex = r'^static/(?P<path>.*)$'
urlpatterns += patterns('',
    (baseurlregex, 'django.views.static.serve',
    {'document_root':  settings.MEDIA_ROOT}),
)
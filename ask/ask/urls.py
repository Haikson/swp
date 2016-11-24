from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.home', name='home'),
    url(r'^login/', 'qa.views.login', name='login'),
    url(r'^logout/', 'qa.views.logout', name='logout'),
    url(r'^signup/', 'qa.views.signup', name='signup'),
    url(r'^question/(?P<question_pk>\d+)/$', 'qa.views.question', name='question'),
    url(r'^ask/', 'qa.views.ask', name='ask'),
    url(r'^popular/', 'qa.views.popular', name='popular'),
    url(r'^new/', 'qa.views.test'),
)

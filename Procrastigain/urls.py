from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'Main.views.index'),

                       # Login / logout.
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^register/$', 'Main.views.register'),
    (r'^register_success/$', 'Main.views.register_success'),

    # Examples:
     url(r'^writigain/$', 'Writigain.views.index', name='writigain'),
     url(r'^listigain/$', 'Listigain.views.index', name='listigain'),
    url(r'^listigain/completed$', 'Listigain.views.index_completed', name='listigain_completed'),
    url(r'^listigain/add$', 'Listigain.views.add', name='add'),
    url(r'^listigain/(?P<task_id>\d+)/delete$', 'Listigain.views.delete', name='delete'),
    url(r'^listigain/(?P<task_id>\d+)/edit$', 'Listigain.views.edit', name='edit'),
     url(r'^main/$', 'Main.views.index', name='main'),
    url(r'^accounts/my_account/$', 'Main.views.my_account', name='my_account'),
    url(r'^listigain/initialize_quad$', 'Listigain.views.initialize_quad', name='initialize_quad'),
    url(r'^listigain/(?P<task_id>\d+)/(?P<start_time>\d+)/(?P<end_time>\d+)/completed$', 'Listigain.views.completed', name='completed'),
    url(r'^listigain/(?P<task_id>\d+)/(?P<start_time>\d+)/(?P<end_time>\d+)/time_up$', 'Listigain.views.time_up', name='time_up'),
    url(r'^listigain/(?P<task_id>\d+)/(?P<start_time>\d+)/(?P<end_time>\d+)/completed_from_listigain$', 'Listigain.views.completed_from_listigain', name='completed_from_listigain'),
    url(r'^listigain/(?P<task_id>\d+)/(?P<start_time>\d+)/(?P<end_time>\d+)/time_up_from_listigain$', 'Listigain.views.time_up_from_listigain', name='time_up_from_listigain'),
    url(r'^listigain/quad/(?P<task_id>\d+)/$', 'Listigain.views.quad_from_listigain', name='quad_from_listigain'),
    url(r'^listigain/quad$', TemplateView.as_view(template_name="quad.html")),
    url(r'^listigain/quad/completed_break$', TemplateView.as_view(template_name="completed_break.html")),
    url(r'^listigain/quad/time_up_break$', TemplateView.as_view(template_name="time_up_break.html")),
    url(r'^listigain/finished_quad$', TemplateView.as_view(template_name="finished_quad.html")),
    url(r'^listigain/no_tasks$', TemplateView.as_view(template_name="no_tasks.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^team/$', TemplateView.as_view(template_name="team.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),


    # url(r'^Procrastigain/', include('Procrastigain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

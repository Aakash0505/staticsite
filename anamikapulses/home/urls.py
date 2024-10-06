from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'home'

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('lead-create/', views.leadCreate, name='lead_create'),

]



# This is only needed when using runserver.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ] + staticfiles_urlpatterns() + urlpatterns

# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'celery_try.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', views.index,name='index'),
    path('poll_state', views.poll_state,name='poll_state'),
    # url(r'^$', views.index,name='index'),
    # url(r'^poll_state$', views.poll_state,name='poll_state'),
]

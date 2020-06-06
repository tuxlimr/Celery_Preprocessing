from django.urls import path,include
# from django.conf.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'celery_try.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^index/', include('testapp.urls')),
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
]

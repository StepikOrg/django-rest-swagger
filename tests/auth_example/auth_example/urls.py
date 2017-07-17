from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include('auth_example.restapi.urls', namespace="cigars")),
    (r'^', include('rest_framework_swagger.urls', namespace='swagger'))
]

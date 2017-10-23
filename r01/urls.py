from django.conf.urls import url
from r01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login', views.login),
]

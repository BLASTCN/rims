from django.conf.urls import url
from r01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login', views.login),
    # url(r'^index', views.home),
    url(r'^sensor', views.sensor),
    url(r'^state', views.state),
    url(r'^envir', views.envir),
    url(r'^result', views.data_result),
    url(r'^tactic', views.tactic),
]

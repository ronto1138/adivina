from django.conf.urls import url
from usrcontrol import views


urlpatterns = [
    url('^$',views.users,name="users"),
]

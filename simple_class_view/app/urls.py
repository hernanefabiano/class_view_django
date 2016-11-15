from django.conf.urls import url
from django.contrib import admin
from application import views
urlpatterns = [
	url(r'^', views.FrontPageHandler.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]

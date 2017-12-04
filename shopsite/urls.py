"""shopsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import  settings
from django.conf.urls.static import static

# from shop import view
from shop import views
from shop.view import user

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/', user.login, name='login'),
    url(r'^register', user.register, name='register'),
    url(r'^detail/(.*?)/$', views.detail, name='detail'),
    url(r'^addcart/$', views.addcar, name='addcart'),
    url(r'^download/$', views.download, name='download'),
    url(r'^querycar/$', views.queryCar, name='querycar'),
    url(r'^cart/$', views.cartView, name='cartView'),
    url(r'^addgood/$', views.addgood, name='addgood')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

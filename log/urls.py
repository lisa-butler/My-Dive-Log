"""log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from log import views
from django.conf.urls import include

app_name = "diveLog"
# this allows us to use the say hello function inside the urls file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_logs/', views.get_logpage, name='get_logpage'),
    path('log_a_dive/', views.log_a_dive, name='log_a_dive'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('delete/<item_id>', views.delete_item, name='delete'),
    path('get_home/', views.get_home, name="get_home"),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
from log import views


app_name = "diveLog"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_logs/', views.get_logpage, name='get_logs'),
    path('log_a_dive/', views.log_a_dive, name='log_a_dive'),
    path('edit/<item_id>', views.edit_item, name='edit_item'),
    path('delete_item/<item_id>', views.delete_item, name='delete_item'),
    path('get_home/', views.get_home, name="get_home"),
    path('logout/', views.logout, name='logout'),
    path('registration/', include('django.contrib.auth.urls')),
    path("register_user", views.register_request, name="register_user"),
    path('diving_officer_home/', views.diving_officer_home, name='diving_officer_home'),
    path('get_club_logs/', views.get_club_logs, name='get_club_logs'),
    path('club_members/', views.club_members, name='club_members'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


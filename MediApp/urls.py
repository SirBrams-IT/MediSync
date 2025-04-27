
from django.contrib import admin
from django.urls import path
from .views import ProgramCreateView, ClientCreateView, ClientListView, enroll_client, search_client, client_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProgramCreateView.as_view(), name='program-create'),
    path('clients/', ClientCreateView.as_view(), name='client-create'),
    path('list/', ClientListView.as_view(), name='list_clients'),
    path('enroll/', enroll_client, name='enroll-client'),
    path('search/<str:name>/', search_client, name='search-client'),
    path('profile/<int:id>/', client_profile, name='client-profile'),
]

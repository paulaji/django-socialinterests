from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add our app urls in the main urls
    path('', include('website.urls')),
]

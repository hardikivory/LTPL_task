

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('order_app.urls')),
    path('accounts/', include('signup_app.urls')),
]

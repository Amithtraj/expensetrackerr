from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tracker/', include('tracker.urls', namespace='tracker')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('', include('accounts.urls'))
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]


from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#change admin panel details
admin.site.site_header = "BlogSpot Admin"
admin.site.site_title = "BlogSpot Admin Panel"
admin.site.index_title = "Welcome to BlogSpot Admin Panel"

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    path('api/', include('api.urls'), name='api'),
    path('api2/', include('api2.urls'), name='api2'),
    path('api_auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^api_doc$', get_swagger_view(title='Rest API Document')),
]

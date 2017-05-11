from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^routers/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

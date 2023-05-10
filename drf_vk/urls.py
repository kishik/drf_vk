from django.template.defaulttags import url
from django.urls import include, path, re_path
from rest_framework import routers
from quickstart import views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'requests', views.RequestViewSet)
router.register(r'friends', views.FriendsViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^openapi-schema', get_schema_view(
    #     title="drf_vk",  # Title of your app
    #     description="test api",  # Description of your app
    #     version="1.0.0",
    #     public=True,
    # ), name='openapi-schema'),
]

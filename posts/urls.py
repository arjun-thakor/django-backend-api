from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('posts/<uuid:pk>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='detail_view')
]
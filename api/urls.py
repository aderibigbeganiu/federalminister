from django.urls import path, include
from rest_framework import routers
from ministries.views import MinistriesViewSet

router = routers.DefaultRouter()
router.register('ministries', MinistriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

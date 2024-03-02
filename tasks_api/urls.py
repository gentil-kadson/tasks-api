from django.urls import path, include
from rest_framework import routers

from tasks_api.to_do_api import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]

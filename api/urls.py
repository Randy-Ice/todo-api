from django.urls import path
from todo.views import TodoViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('todo', TodoViewSet)
urlpatterns = router.urls

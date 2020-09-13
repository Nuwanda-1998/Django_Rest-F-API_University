from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from .views import TopicsList, LocationList, classhList,TopicDetail, FieldViewset, TopicViewset
from . import views

router = DefaultRouter()
router.register('fields', views.FieldViewset)
router.register('topics', views.TopicViewset)
router.register('locations', views.LocationViewset)
router.register('classes', views.classViewset)
router.register('users', views.UserUViewset)


app_name = 'classes'


urlpatterns = [
    path('', include(router.urls)),
]

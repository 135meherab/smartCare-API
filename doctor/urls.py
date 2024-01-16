from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('list', views.DoctorViewSet)
router.register('designation', views.DesignationViewSet)
router.register('specialisation', views.SpecialisationViewSet)
router.register('review', views.ReviewViewSet)
router.register('availabletime', views.AvailableTimeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

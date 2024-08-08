from django.urls import path
from .views import TestList, BolimList

urlpatterns = [
    path('tests/', TestList.as_view(), name='test-list'),
    path('bolims/', BolimList.as_view(), name='bolim-list'),

]

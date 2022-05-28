from django.urls import include, path

from .views.customer import CustomerView

urlpatterns = [
    path(
      'v1/customer/',
      CustomerView.as_view()
    ),
    path(
      'v1/customer/<int:pk>/',
      CustomerView.as_view()
    ), 
]

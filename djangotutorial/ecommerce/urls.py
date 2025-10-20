from django.urls import path

from . import views

app_name = "ecommerce"
urlpatterns=[
    path("user",views.OrderUserView.as_view(), name="order-user"),
]

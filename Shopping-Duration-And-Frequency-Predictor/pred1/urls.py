from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predict_shopping_duration/duration_predict', views.duration_predict, name="duration_predict"),
    path('predict_shopping_amount/amount_predict', views.amount_predict, name="amount_predict"),
    path('predict_shopping_amount/', views.amount_render, name="amount_render" ),
    path('predict_shopping_duration/', views.duration_render, name="duration_render")
]
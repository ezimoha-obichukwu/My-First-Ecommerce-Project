from django.urls import path
from .  import views

urlpatterns = [
    path('', views.product_page, name="product-page"),
    path('about/', views.about, name="about"),
    path("<int:id>/", views.single_product_view, name='single')
]
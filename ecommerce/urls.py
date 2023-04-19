from django.urls import path
from .  import views

urlpatterns = [
    path('', views.product_page, name="product-page"),
    path('about/', views.about, name="about"),
    path("<int:id>/", views.single_product_view, name='single'),
    path('latest-post/', views.latest_post, name="latest_post"),
    path("<int:pk>/latest-post-details", views.single_latest_post, name="latest_details"),
    path('announcement-page/', views.announcement_page, name="announcements"),
    path('calendar-page/', views.calendar_page, name="calendars")
]
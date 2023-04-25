from django.contrib import admin
from django.urls import path
from trucks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("trucks/", views.index, name="index"),
]

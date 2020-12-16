from . import views
from django.urls import path

#
urlpatterns = [
    path("", views.owners, name='owners'),
    path("further/", views.index2, name='index2')
]
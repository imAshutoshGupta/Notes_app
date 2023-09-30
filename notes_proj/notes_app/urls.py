from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dash),
    path('addnotes', views.create),
    path('updatenotes/<rid>', views.update),
    path('deletenotes/<rid>', views.delete),
]
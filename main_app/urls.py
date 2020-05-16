from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('widgets/add_widget/', views.add_widget, name='add'),
    path('widgets/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete'),
]
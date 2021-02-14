from django.urls import path

from . import views

app_name = 'costs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail')
]

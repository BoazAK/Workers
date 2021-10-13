from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_form, name = 'worker_insert'),
    path('<int:id>/', views.worker_form, name = 'worker_update'),
    path('delete/<int:id>/', views.worker_delete, name = 'worker_delete'),
    path('list/', views.worker_list, name = 'worker_list'),
]

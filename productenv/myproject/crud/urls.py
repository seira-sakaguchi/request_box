from django.urls import path

from .import views

app_name = 'crud'
urlpatterns = [
    path('list/',views.ProductListView.as_view(), name='list'),
    path('new/',views.ProductCreateView.as_view(), name='new'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]

    
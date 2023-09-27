from django.urls import path
from . import views
from .views import redirect_view

urlpatterns = [
    path('', views.ind, name='index-page'),
    path('signup/', views.signup, name='signup-page'),
    path('prediction/', views.prediction, name='prediction-page'),
    path('prediction/', views.redirect_view)

]

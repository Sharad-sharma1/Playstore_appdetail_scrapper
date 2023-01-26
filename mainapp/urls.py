
from django.urls import path
from . import views

urlpatterns = [
    path('celerynew/', views.celerytest, name="test")
]
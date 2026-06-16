from django.urls import path
from . import views

app_name='intro_app'

urlpatterns=[
    path('intro',views.First_intro,name='intro')
]
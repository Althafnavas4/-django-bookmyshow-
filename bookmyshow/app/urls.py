from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('movie',views.movie),
    path('LuckyBaskhar',views.LuckyBaskhar),


    # ---------------shop--------------------


]
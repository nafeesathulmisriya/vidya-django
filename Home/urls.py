
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='Home'),
    path('about',views.about,name='about'),
    path('show',views.show,name='show'),
    path('basecall',views.base),
    path('dept',views.base,name='dept'),
    path('doctor',views.Doctors,name='doctor'),
    path('booking',views.booking),
]

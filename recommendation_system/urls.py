from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('system',views.system,name='system'),
    path('print_result',views.print_result,name='print_result')
]
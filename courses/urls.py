from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('', students, name='home1'),
    path('', teachers, name='home2'),
    # path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    # path('contact/', contact, name='contact'),
    # path('login/', login, name='login'),
]

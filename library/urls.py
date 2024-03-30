from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path ('authorisation', views.authorisation, name ='authorisation'),
    path('junior', views.junior, name='junior'),
    path('senior', views.senior, name='senior'),
    path('lower', views.lower, name='lower'),
    path('jbooks', views.jbooks, name='jbooks'),
    path('sbooks', views.sbooks, name= 'sbooks'),
    path('lbooks', views.lbooks, name= 'lbooks'),
    path('bsearched', views.bsearched, name= 'bsearched'),
    path('psearched', views.psearched, name= 'psearched'),
    #path('totalbooks', views.totalbooks, name= 'totalbooks'),
]
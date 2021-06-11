from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('produit',produit, name='produit'),
    path('categorie',categorie, name='categorie'),
    path('about',about,name='about'),
    path('register',register, name='register'),
    path('learnmore/<int:idp>', learnmore, name='learnmore'),
    path('liker/<int:id_p>', liker, name='liker'),
    path('page_membre/<str:email>', page_membre, name='page_membre'),
    path('login', login, name='login'),
]
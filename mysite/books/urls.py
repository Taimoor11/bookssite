from django.urls import path
from . import views
from .views import contact
from django.contrib.auth import views as auth_views



app_name = 'books '

urlpatterns=[
    path('',views.homepage, name='home_page'),
    path('books/',views.books_list, name='books_list',),
    path('searchform/', views.search_form),
    path('searchresult/', views.dosearch),
    path('<int:id>/<slug:slug>', views.book_detail, name='book_detail')

]
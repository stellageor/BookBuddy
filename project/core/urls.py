from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/settings/', views.account_settings, name='account_settings'),
    path('account/chang-password/', views.change_password, name='change_password'),
    
    path('my-books/', views.my_books, name='my_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
    path('', views.book_search, name='home'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),  # URL for editing a book

    path('books/<int:book_id>/borrow/', views.create_borrowing, name='create_borrowing'),
    path('my-borrowings/', views.my_borrowings_view, name='my_borrowings'),path('books/<int:book_id>/return/', views.return_book, name='return_book'),

]

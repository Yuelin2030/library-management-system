from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Articles
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_new, name='article_new'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),

    # Members
    path('members/', views.member_list, name='member_list'),
    path('member/<int:pk>/', views.member_detail, name='member_detail'),
    path('member/new/', views.member_new, name='member_new'),
    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('member/<int:pk>/delete/', views.member_delete, name='member_delete'),

    # Transactions
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transaction/new/', views.transaction_new, name='transaction_new'),
    path('transaction/<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # Settings
    path('settings/', views.library_settings_view, name='library_settings'),
]
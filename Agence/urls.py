from django.urls import path
from . import views
from Agence.views import index, suite_detail, cart, add_to_cart, delete_cart, about, contact, cart_detail, new_suite, SuiteList



urlpatterns = [
    path('',index, name="index"),
    path('about/',about, name="about"),
    path('contact/',contact, name="contact"),
    path('search/',views.search, name="search"),
    path('thank_you/<int:total_price>/', views.thank_you, name='thank_you'),
    path('order_summary/',views.order_summary, name="order_summary"),
    path('validate_cart/',views.validate_cart, name="validate_cart"),
    path('cart/',cart, name="cart"),
    path("suite_list/", SuiteList.as_view(), name="suite_list"),
    path('suite/<slug:slug>/', suite_detail, name="suite"),
    path('cart_detail/', cart_detail, name="cart_detail"),
    path('cart/delete/', delete_cart, name="delete_cart"),
    path('new_suite/', new_suite, name="new_suite"),
    path("update/<str:slug>", views.update_suite, name="update_suite"),
    path('delete/<slug:slug>', views.delete_suite, name="delete_suite"),
    path('suite/<slug:slug>/add-to-cart/', add_to_cart, name="add-to-cart")
]





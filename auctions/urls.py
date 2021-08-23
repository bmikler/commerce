from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("auction/<str:page>", views.auction_page, name="auction_page"),
    path("categories", views.categories, name="categories"),
    path("categories_listing/<str:category>", views.categories_listing, name="categories_listing"),

]

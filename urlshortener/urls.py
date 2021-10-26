from django.urls import path
from urlshortener.views import create_view, redirect_view, hit_link

appname = "urlshortener"

urlpatterns = [
    path("create", create_view, name="create"),
    path("s/<str:shortened_url>", redirect_view, name="redirect"),
    path("hit/<str:shortened_url>", hit_link, name="hit")
]

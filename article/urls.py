from django.urls import path
from article import views 

urlpatterns = [
    path("article",views.article,name="article"),
]

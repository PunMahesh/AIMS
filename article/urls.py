from django.urls import path
from article import views 

urlpatterns = [
    path("article",views.add_article,name="article"),
    path("get_article",views.get_article,name="get_article"),
]

from django.shortcuts import render, redirect
from .models import Article
from django.core.files.storage import FileSystemStorage

# Create your views here.
def add_article(request):
    if request.method == "POST":
        user = request.user
        ArticleName = request.POST.get("ArticleName")
        Article_Photo = request.FILES.get("Article_Photo")
        Description = request.POST.get("Description")

        details = Article(user=user,ArticleName=ArticleName, Article_Photo=Article_Photo, Description=Description)
        details.save()
        return redirect("Articel_added")
    return render(request, 'article.html')

def get_article(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    print (context)
    return render(request, 'blog.html', context)
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import News, Category,Comment
def home(request):
    first_news=News.objects.last()
    three_news=News.objects.all()[::-1]
    three_categories=Category.objects.all()[::]
    return render(request,'home.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

# All News
def all_news(request):
    all_news=News.objects.all()[::-1]
    return render(request,'all-news.html',{
        'all_news':all_news
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted but in moderation mode.')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)[::-1]
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    }) 

# Fetch all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })



# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)[::-1]
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

def about(request):
    return render(request , 'about.html')
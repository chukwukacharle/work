from django.shortcuts import render
from .models import post

posts = [
    {
        'author': 'Chris',
       ' title': 'Blog post 1',
       ' content': 'first post content',
       'dated_posted':'August 23 2015',
    },
    {
        'author': 'Charles',
       ' title': 'Blog post 2',
       ' content': 'second post content',
       'dated_posted':'september 29 2017',
    },
]



def home(request):
    context = {
        'posts': post.objects.all(),
    }
    return render(request, 'buck/home.html', context )
def about(request):
    return render(request, 'buck/about.html', {'title': 'About'} ) 
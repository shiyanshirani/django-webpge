from django.shortcuts import render

posts = [
    {
        'author': 'Shiyan Shirani',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'June 16, 2021'
    },
    {
        'author': 'Anandita Puria',
        'title': 'Blog Post 2',
        'content': 'First Post Content',
        'date_posted': 'June 17, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'}) 
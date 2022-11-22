from django.shortcuts import render
from .models import Post

# Create your views here.
def index (request):
    posts = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    context = {
        'title':'Blog | Hekal',
        'heading':'Welcome To My Blog',
        'body':'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore distinctio, amet repellendus tempore totam reprehenderit ratione quasi, corporis possimus modi expedita voluptatum saepe ipsum et! Commodi amet error temporibus dolorum.',
        'posts':posts,
        'categoriesPost':categories,
    }

    return render (request,'blog/index.html',context)


def categoryPost (request,categoryInput):
    posts = Post.objects.filter(category=categoryInput);
    categories = Post.objects.values('category').distinct();
    print(categories);
    context = {
        'title':'Blog | Hekal',
        'heading':'Category',
        'body':'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore distinctio, amet repellendus tempore totam reprehenderit ratione quasi, corporis possimus modi expedita voluptatum saepe ipsum et! Commodi amet error temporibus dolorum.',
        'posts':posts,
        'categoriesPost':categories,
    }

    return render (request,'blog/category.html',context)

def detailPost (request,slugInput):
    posts = Post.objects.get(slug=slugInput);
    categories = Post.objects.values('category').distinct();
    context = {
        'title':'Blog | Hekal',
        'heading':'Welcome To My Blog',
        'body':'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore distinctio, amet repellendus tempore totam reprehenderit ratione quasi, corporis possimus modi expedita voluptatum saepe ipsum et! Commodi amet error temporibus dolorum.',
        'posts':posts,
        'categoriesPost':categories,
    }

    return render (request,'blog/detail.html',context)
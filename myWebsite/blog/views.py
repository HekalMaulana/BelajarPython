from django.shortcuts import render
from .forms import contactForm
from .models import postModels

# Create your views here.


def index (request):
    posts = postModels.objects.all()
    context = {
        'title':'Blog | Hekal',
        'subtitle':'Welcome To My Blog',
        'posts':posts
    }
    return render(request,'blog/index.html',context)

def contact (request):
    form = contactForm()

    if request.method == 'POST':
        postModels.objects.create(
            Nama = request.POST['Nama_Lengkap'],
            email = request.POST['email'],
            alamat = request.POST['alamat'],
        )

    context = {
        'title':'Contact | Hekal',
        'subtitle':'Welcome To My Contact',
        'form':form,
    }

    # print(request.POST['Nama_Lengkap'])
    # print(request.POST['email'])
    return render(request,'blog/Contact.html',context)
from django.shortcuts import render

def index (request):
    context = {
        'title':'Home | Hekal',
        'subtitle':'Welcome To My Home'
    }
    return render(request,'index.html',context)
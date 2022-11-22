from django.shortcuts import render

def index (request):
    context = {
        'title':'Home | Hekal',
        'heading':'Welcome To My Home',
        'body':'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore distinctio, amet repellendus tempore totam reprehenderit ratione quasi, corporis possimus modi expedita voluptatum saepe ipsum et! Commodi amet error temporibus dolorum.',
    }

    return render(request,'index.html',context)
from django.shortcuts import render,redirect,get_object_or_404
#
from msceapp.models import setting,ContactForm,ContactMassage
# 
from ProjectApp.models import ConstractionCatagory, ConstractionProject
# Create your views here.

def index(request):
    settings = get_object_or_404(setting, id=1)
    slide_img = ConstractionProject.objects.all().order_by('-id')[:4]
    context = {
        'settings':settings,
        'slide_img':slide_img
    }
    return render(request, 'index.html', context)

def home(request,id):
    settings = setting.objects.get(id=id)
    context = {   
        'settings':settings
    }
    return render(request, 'index-2.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMassage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.massage = form.cleaned_data['massage']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            return redirect('Know')
    form = ContactForm
    settings = setting.objects.get(id=1)
    context = {
        'form':form,
        'settings':settings
    }

    return render(request, 'contact.html',context)

def service(request):
    return render(request, 'services-1.html')

def singel_post(request,id):
    settings = get_object_or_404(setting, id=1)
    single_Pro =  get_object_or_404(ConstractionProject, id=id)
    context = {
        'settings':settings,
        'single_pro':single_Pro
    }
    
    return render(request, 'project-single.html',context)

def about(request):
    settings = get_object_or_404(setting, id=1)
    context = {
        'settings':settings,
       
    }
    return render(request, 'about-us.html',context)
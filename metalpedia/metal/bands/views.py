from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Band
from .models import News
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    news_list = News.objects.all().order_by('-pub_date').values()
    context={'news_list': news_list,}
    return render(request,'bands/index.html',context)

def bands(request):
    bands_list= Band.objects.all().order_by('name').values()
    context = {'bands_list': bands_list,}
    return render(request, 'bands/bands.html',context)
    
def specificBand(request, id):
    bands_list= Band.objects.get(id=id)
    template = loader.get_template('bands/viewBand.html')
    context={'bands_list': bands_list,}
    return HttpResponse(template.render(context,request))

def about(request):
    return render(request,'bands/about.html')

@login_required(login_url='/metalpedia/login/')
def add(request):
    return render(request,'bands/add.html')

def addband(request):
    a = request.POST['name']
    b = request.POST['genre']
    c = request.POST['country']
    d = request.POST['status']
    e = request.POST['formed']
    f = request.POST['notes']
    g = request.user
    band = Band(name=a,genre=b,country=c,status=d,formed=e,notes=f,user=g)
    band.save()
    return HttpResponseRedirect(reverse('index'))   
    
def specificNews(request,id):
    news_list= News.objects.get(id=id)
    template = loader.get_template('bands/viewNews.html')
    context={'news_list': news_list,}
    return HttpResponse(template.render(context,request))

def login(request):
    if request.method == "GET":
       return render(request,'bands/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('psw')
        
        user = authenticate(username=username,password=password)
        
        if user:
            auth_login(request,user)
            messages.success(request,("you are logged"))
            return redirect('index')
        else:
            messages.warning(request,'username or password invalid')
            return redirect('login')

def register(request):
    if request.method == "GET":
        return render(request,'bands/register.html')
    else:
        username = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            messages.error(request,'username already registered')
            return redirect('register')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        auth_login(request,user)
        messages.success(request,("user registered"))
        return redirect('index')
    
    
def logout_user(request):
    logout(request)
    messages.success(request,("you were logged out"))
    return redirect('index')

def profile(request):
    user = request.user
    bandsAdded = Band.objects.filter(user=request.user)
    template = 'bands/profile.html'
    return render(request,template,{'bandsAdded':bandsAdded,'user':user})


def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request,("account deleted"))
    return redirect('index')
    
#def pagination(request):
    #bands_list = Band.objects.all()
    #paginator = Paginator(bands_list,5)
    #band_number = request.GET.get('page')
    #page_obj = paginator.get_page(band_number)
    #return render(request, 'bands/bands.html',{'page_obj': page_obj})
    
#class bandsListView(ListView):
    #paginate_by = 5
    #model = Band
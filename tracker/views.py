from django.shortcuts import render,redirect
from . models import Tracker,Driver,Chat
from .forms import DriverForm,TrackerForm,ChatForm
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    tracker = Tracker.objects.all()
    jobs_count = Tracker.objects.count()
    return render (request, 'tracker/home.html',{'tracker':tracker,'jobs_count':jobs_count})


# this is for completing jobs
def delete(request,id):
    tracker = Tracker.objects.get(id=id)
    tracker.delete()
    return redirect('index')
    
def addDriver(request):
    context ={}
    form = DriverForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('drivers')  
        
    context['form'] = form

    return render(request,'tracker/add_driver.html',context)  
def addJob(request):
    context ={}
    form = TrackerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context['form'] = form
    return render(request,'tracker/add_job.html',context)



# see all drivers
def driver(request):
    drivers = Driver.objects.all()
    drivers_count = Driver.objects.count()
    return render(request,'tracker/drivers.html',{'drivers':drivers,'drivers_count':drivers_count})


# update tracker 
def update(request, id):  
    tracker = Tracker.objects.get(id=id)  
    form = TrackerForm(instance = tracker) 

    if request.method == 'POST':
        form = TrackerForm(request.POST,instance=tracker)
        if form.is_valid():  
            form.save()  
            return redirect("index")  
    return render(request, 'tracker/update_tracker.html', {'form': form})  


def updateDriver(request, id):  
    driver = Driver.objects.get(id=id)  
    form = DriverForm(instance = driver) 

    if request.method == 'POST':
        form = DriverForm(request.POST,instance=driver)
        if form.is_valid():  
            form.save()  
            return redirect("drivers")  
    return render(request, 'tracker/update_driver.html', {'form': form})  



def deleteDriver(request,id):
    driver = Driver.objects.get(id=id)
    driver.delete()
    return redirect('drivers')

def chats(request):
    chat = Chat.objects.all()
    chats_count = Chat.objects.count()
    return render(request, 'tracker/chats.html',{'chat':chat,'chats_count':chats_count})


def addChat(request):
    context ={}
    form = ChatForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('chats')
    context['form'] = form
    return render(request,'tracker/add_chat.html',context)


def deleteChat(request,id):
    chat = Chat.objects.get(id=id)
    chat.delete()
    return redirect('chats')   

def updateChat(request, id):  
    chat = Chat.objects.get(id=id)  
    form = ChatForm(instance = chat) 

    if request.method == 'POST':
        form = ChatForm(request.POST,instance=chat)
        if form.is_valid():  
            form.save()  
            return redirect("chats")  
    return render(request, 'tracker/update_chat.html', {'form': form})  

def loginUser(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)

        except:
            # messages.error(request,'username or password incorrect')
            user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'username or password incorrect')

    return render(request, 'tracker/login.html')

def logoutUser(request):
    logout(request)
    return redirect('index')



def register(request):
    form = UserCreationForm()  
    if request.POST == 'POST':  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')
            return redirect('index')   
        else:  
            form = UserCreationForm()  
    
    return render(request, 'tracker/register_user.html', {'form':form})  


def history(request):
    history = Tracker.objects.all()
    return render(request, 'tracker/job_history.html',{'history':history})
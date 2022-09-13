from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import UploadImageForm
from myapp.models import UploadImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
# # @login_required(login_url='front')
# def home(request):
#     if request.method == "POST":
#         form=UploadImageForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.user = request.user
#             note.save()
#             obj=form.instance
#                 # to show what we upload
#                 # return render(request,"index.html",{"obj":obj})
#             return redirect('home')
#     else:
#         form=UploadImageForm()
#     user=request.user
#     img=UploadImage.objects.all()
#     myimages=UploadImage.objects.filter(user=user)
#     random=UploadImage.objects.order_by('?').first()
#     last_three = UploadImage.objects.all().order_by('-id')[:3]
#         # we use img in index file to display all images uploaded by for loop
#     return render(request,"index.html",{"img":img,"form":form,"random":random,"last_three":last_three})
@login_required(login_url='signin')
def home(request):
     if request.user.is_authenticated:
        form=UploadImageForm()
        user=request.user
        img=UploadImage.objects.all()
        myimages=UploadImage.objects.filter(user=user)
        random=UploadImage.objects.order_by('?').first()
        last_three = UploadImage.objects.all().order_by('-id')[:3]
        # we use img in index file to display all images uploaded by for loop
        return render(request,"index.html",{"img":img,"form":form,"random":random,"myimages":myimages,"last_three":last_three})


@login_required(login_url='signin')
def add_image(request):
    if request.user.is_authenticated:
        user = request.user
        form = UploadImageForm(request.POST,request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else: 
            return render(request , 'index.html' , {'form' : form})

            


def front(request):
    user=request.user
    img=UploadImage.objects.all()
    random=UploadImage.objects.order_by('?').first()
    last_three = UploadImage.objects.all().order_by('-id')[:3]
        # we use img in index file to display all images uploaded by for loop
    return render(request,"front.html",{"img":img,"random":random,"last_three":last_three})

def signup(request):
    if request.method == 'POST':
        fm=UserCreationForm(request.POST or None)
        if fm.is_valid():
            messages.success(request,'Account created Successfully')
            user=fm.save()
            if user is not None:
                return redirect('/signin/')
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})

def signin(request):
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    loginUser(request, user)
                    messages.success(request,'Successfully logged in!')
                    return redirect('home')
        else:
            fm=AuthenticationForm()
        return render(request, 'signin.html',{'form':fm})

def signout(request):
    logout(request)
    return redirect('front')
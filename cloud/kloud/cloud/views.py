from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from cryptography.fernet import Fernet
import secrets
import string
import bcrypt

from .models import *
# Create your views here.
salt = bcrypt.gensalt()




def EncryptPwd(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encPwd = fernet.encrypt(password.encode())
    print(encPwd)
    return encPwd


def DecryptPwd(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    decPwd = fernet.decrypt(password.encode())
    print(decPwd)
    
    return decPwd


def Register(request):
    N = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
    for i in range(N))
    user = UserModel()
    if request.method=='POST':
        fullname = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd').encode()
        repwd = request.POST.get('repwd').encode()
        if pwd !=repwd:
            print("Password Mixmatch")
            # pwd= EncryptPwd(pwd)
            print(pwd)
        elif user.Username == username:
            print("Username already Exists")
        else:
            # hashPwd = bcrypt.hashpw(pwd, salt)
            user.Fullname = fullname.lower()
            user.Email = email.lower()
            user.Username = username.lower()
            user.Unique_Number = str(res)
            user.Password = make_password(pwd)
            # print(user.Password)
            user.save()
            # print(salt, '....', hashPwd)
            return redirect('login')
            
            
            
# print result
    # print("The generated random string : " + str(res))

    return render(request, 'cloud/register.html')
    
def Login(request):
    # usrPwd =  user.Password.encode()
    if request.method=='POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user = UserModel.objects.get(Username=name)
        userPwd = check_password(pwd, user.Password)
        # salt = bcrypt.gensalt()
        # user = authenticate(Username = name, Password = pwd)
        if user:
            print("user Exist")
            # pwd = DecryptPwd(pwd)
            if userPwd:
               print("user Active")
               return redirect('dashboard')
            else:
                print("user inactive")

        else:
             print("Does not exist")
            

    return render(request, 'cloud/login.html')



def Logout(request):
     logout(request)
     return redirect('login')
        

@login_required(login_url='login')
def Dashboard(request):
    
    return render(request, 'cloud/dashboard.html')


@login_required(login_url='login')
def AddPost(request):
        newPost = UserPosts()
        if request.method == 'POST':
            name = request.POST.get('name')
            category = request.POST.get('category')
            # img = request.FILES['img']
            # print(name, category, img)
            newPost.Name  = name
            newPost.Category = category
            newPost.PostImage = request.FILES['image']
            newPost.save()
            return redirect('view-post')
            
        return render(request, 'cloud/addpost.html')

@login_required(login_url='login')
def ViewPost(request):
    Posts = UserPosts.objects.all()
    i=1
    context = {'Posts':Posts, 'i':i}
    return render(request, 'cloud/view-post.html', context)

@login_required(login_url='login')
def Videos(request):
    Posts = UserPosts.objects.all()
    videos = Posts.filter(Category='Videos').order_by('created_at')[0:4]
    context = {'videos':videos}
    return render(request, 'cloud/videos.html', context)

@login_required(login_url='login')
def Images(request):
    Posts = UserPosts.objects.all()
    images = Posts.filter(Category='Images').order_by('created_at')[0:4]
    context = {'images':images}
    return render(request, 'cloud/Images.html', context)
@login_required(login_url='login')
def Documents(request):
    Posts = UserPosts.objects.all()
    documents = Posts.filter(Category='Documents').order_by('created_at')[0:4]
    context = {'documents':documents, 'Posts' :Posts}
    return render(request, 'cloud/documents.html', context)
    
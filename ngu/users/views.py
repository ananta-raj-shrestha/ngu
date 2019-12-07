from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile,UserEditForm,ProfileEditForm



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if first_name != ''and last_name !='' and username != '' and email!= '' and password != ''  :
           if (password != cpassword):
                messages.info(request,f'Enter Same password!')
                
           else: 
                if(User.objects.filter(username=username).exists()):
                    messages.info(request,f'The username {username} already exists!') 
                elif(User.objects.filter(email=email).exists()):
                    messages.info(request,f'The email {email} already exists!')   
                else:
                    new_user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    new_user.save()
                    Profile.objects.create(user=new_user)
                    messages.success(request,f'Account created for {username}!')
                    return redirect('login')
       
        else:
           messages.warning(request,'Please fill all field!')
 
    return render(request,'users/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,f'You are login successfully!') 
            return redirect('blog-index')
        else:
            messages.warning(request,f'Username or Password is wrong!') 
            return redirect('login')
    else:

       return render(request,'users/login.html')
def logout(request):
     auth.logout(request)
     messages.success(request,f'You are logout successfully!')
     return redirect('blog-index')
def profile(request):
      if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if first_name != ''and last_name !='' and username != '' and email!= '' and password != ''  :
           if (password != cpassword):
                messages.info(request,f'Enter Same password!')
                
           else: 
                if(User.objects.filter(username=username).exists()):
                    messages.info(request,f'The username {username} already exists!') 
                elif(User.objects.filter(email=email).exists()):
                    messages.info(request,f'The email {email} already exists!')   
                else:
                    user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                    user.save()
                    messages.success(request,f'Account created for {username}!')
                    return redirect('login')
       
        else:
           messages.warning(request,'Please fill all field!')
 
      return render(request,'users/profile.html')
def update(request):
    user_form = UserEditForm(data=request.POST or None,instance=request.user)
    profile_form = ProfileEditForm(data = request.POST or None,instance = request.user.profile,files =request.FILES)
    if request.method =='POST':
       
        if user_form.is_valid and profile_form.is_valid:
            profile_form.save()
            user_form.save()
            return redirect('profile')
        else:
            user_form=UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance = request.user.profile)
            return redirect('edit')
            
    dic={
                'user_form':user_form,
                'profile_form':profile_form
            }
    return render(request,'users/update.html',dic)
    


    

     
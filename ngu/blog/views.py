from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,BadHeaderError
from  .models import posts,PostEditForm, PostCreateForm,Comment
from django.db.models import Q
from django.forms import modelformset_factory
from django.contrib.auth.models import User,auth
from django import forms
from .forms import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail

# posts=[
#     {
#         'author':'ananta raj shrestha',
#         'title' :'SAG',
#         'content':'SAG stands for South Asian Game',
#         'date':'2019,Dec 04'
#     },
#      {
#         'author':'ananta raj shrestha',
#         'title' :'SAG',
#         'content':'SAG stands for South Asian Game',
#         'date':'2019,Dec 04'
#     }
# ]
def post_delete(request,id):
    post = posts.objects.get(id=id)
    if request.user != post.author:
         raise Http404
    post.delete()
    return redirect('blog-index')

def post_upload(request):
    admin = User.objects.get(username='nevergiveup')
    if request.user != admin:
            raise Http404('You are seems to be goining to do illegal work!    -Messages By admin ' )
    if request.method == "POST":
        
        form = PostCreateForm(request.POST)
      
        if form.is_valid() :
              post = form.save(commit=False)
              post.author = request.user
              post.save()
              return redirect('blog-index')
              
    else:
        form=PostCreateForm()
    dic =  {
          'form':form,
       
    }

    return render(request,'blog/post_upload.html',dic)

def post_edit(request,id):
    post = posts.objects.get(id=id)
    post_form = PostEditForm(data=request.POST or None,instance=post)
    if post.author != request.user:
        raise Http404
    if request.method == 'POST':
        
        if post_form.is_valid():
            post_form.save()
            return redirect('blog-index')
        else:
            post_form=PostEditForm(instance=post)
    dic =  {
          'form':post_form,
          'post':post
        }
    return render(request,'blog/post_edit.html',dic)


def post_detail(request,id):
    post = posts.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by('-id')
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post,user=request.user,content=content)
            comment.save()

    dic={
        'post':post,
        'comment_form':comment_form,
        'comment':comments,
        'title':'@ngu-post-detail'

    }
    return render(request,"blog/view.html",dic)
def success(request):
    return HttpResponse('Success! Thank you for your message.')

def index(request):
    if request.method =="POST":
        subject = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
       
        try:
            send_mail(  subject,comment,email,['eranantarajshrestha@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')
    post_list = posts.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query :
        post_list = posts.objects.filter(Q(title__icontains=query)|Q(author__username__icontains=query))
    paginator = Paginator(post_list,3)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    dic ={
        'posts':post
    }
    return render(request,"blog/web.html",dic)
# def login(request):
#     return render(request,"blog/login.html",{'title':'Login'})
# def register(request):
#     return render(request,"blog/register.html",{'title':'Register'})


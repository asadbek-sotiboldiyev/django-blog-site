from django.shortcuts import render,redirect
from .models import Post,Message
from django.core.paginator import Paginator

def HomePageView(request):
	return render(request,'home.html')

def ContactPage(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		message=request.POST['message']
		new_message=Message.objects.create(name=name,message=message,email=email)
		new_message.save()
		return render(request,'contacted.html',{'name':name,'email':email})
	return render(request,'contact.html')

def BlogPageView(request):
	page=int(request.GET.get('page',1))
	posts=Post.objects.all()[::-1]
	pagination=Paginator(posts,6)
	if page>0 and page<=pagination.num_pages:
		posts=pagination.get_page(page)
		posts=posts.object_list
		if page==pagination.num_pages:
			next=False
		else:
			next=page+1
		context={
			'posts':posts,
			'count':range(1,pagination.num_pages+1),
			'previous':page-1,
			'next':next,
			'page':page,
			'page_obj':pagination.get_page(page)
		}
		return render(request,'blog/index.html',context=context)
	return render(request,'404.html')

def PostDetail(request,ID):
	post=Post.objects.filter(id=ID)
	if post.exists():
		post=post[0]
		date=f"{post.data.day}.{post.data.month}.{post.data.year}"
		time=f"{post.data.hour}:{post.data.minute}"
		context={
			'post':post,
			'date':date,
			'time':time
		}
		return render(request,'blog/detail.html',context=context)
	return render(request,'404.html')

def PostCreate(request):
	if request.user.is_staff:
		if request.method=="POST":
			title=request.POST['title']
			summary=request.POST['summary']
			body=request.POST['body']
			new=Post.objects.create(title=title,summary=summary,body=body)
			new.save()
			return redirect('detail',new.id)
		return render(request,'blog/create.html')
	else:
		return render(request,'404.html')

def PostDelete(request,ID):
	if request.user.is_staff:
		post=Post.objects.filter(id=ID)
		if post.exists():
			post=post[0]
			if request.method=="POST":
				post.delete()
				return redirect('blog')
			return render(request,'blog/delete.html',{'post':post})
		return render(request,'404.html')
	return render(request,'404.html')
	
def PostEdit(request,ID):
	if request.user.is_staff:
		post=Post.objects.filter(id=ID)
		if post.exists():
			post=post[0]
			if request.method=="POST":
				title=request.POST['title']
				summary=request.POST['summary']
				body=request.POST['body']
				post.title=title
				post.summary=summary
				post.body=body
				post.save()
				return redirect('detail',post.id)
			return render(request,'blog/edit.html',{"post":post})
		return render(request,'404.html')
	return render(request,'404.html')

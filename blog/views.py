# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.

"""


from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response


from models import Post, Comment 


def post_list(request):
	
	posts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':posts,'user': request.user})
	return HttpResponse(t.render(c))
       


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude=['post','author']




@csrf_exempt
def post_detail(request, id, showComments=False):
	
	posts = Post.objects.get(pk=id)
	
	if request.method == 'POST':
		comment = Comment(post=posts,author=request.session["uname_sess"])
		#Comment.author = request.session["uname_sess"]
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(request.path)
	else:
		form = CommentForm()
	
	comments = posts.comments.all()
	return render_to_response('blog/post_detail.html',{
					'posts':posts,
					'comments':comments,
					'form':form,
					'user': request.user})


	
	
@csrf_exempt	
def edit_comment(request,id):
	comment = Comment.objects.get(pk=id)
	if request.user.username == '':
		return HttpResponseForbidden("You are logged out.<br/><a href='/reg/login'>CLICK TO LOGIN</a>")
	elif comment.author != request.user.username:
		return HttpResponseForbidden("You do not have permission to edit this comment<br/><a href='/blog/posts'>CLICK TO GET BLOGS</a>")
	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(comment.post.get_absolute_url())
	else:
		form = CommentForm(instance=comment)
		
	return render_to_response('blog/edit_comment.html',{'comment':comment,'form':form,'user': request.user})

	
	

	
#search    
def post_search(request, term):
	if request.GET.get('search_item','') != '':
		term = request.GET.get('search_item','')
	posts = Post.objects.filter(title__icontains=term) | Post.objects.filter(body__icontains=term)
	return render_to_response('blog/post_search.html',{'posts':posts,'term':term,'user': request.user})
        
	
def home(request):
	return render_to_response('blog/base.html',{'user': request.user})

# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
        html=''
        for p in Post.objects.all():
                html+='<h2>'+str(p)+'</h2>'+'<br/>'+str(p.body)+'<br/>'
        return HttpResponse(html)
    
    #print type(post_list)
    #print post_list
	#return HttpResponse('This should be a list of posts!')
   

def post_detail(request, id, showComments=False):
	#pass
        p = Post.objects.get(pk=id)
        if bool(showComments) == False:
		return HttpResponse('<h2>'+str(p)+'</h2>'+'<br/>'+str(p.body)+'<br/>')
        else:
		#q = Post.objects.all()[int(id)-1]
		html=''
                #for c in Comment.objects.all().get(post=p):
		html='<h2>'+str(p)+'</h2>'+'<br/>'+str(p.body)+'<br/>'+'<h4>COMMENTS</h4><br\><hr/>'
        	comm=''
		
        	for i in p.comments.all():
			comm+='<i>***Comment***</i>  '+i.body + '<br/><br/>'
		return HttpResponse(html + '<br/>' + comm)        
	

	
    
def post_search(request, term):
        html=''
	p = Post.objects.filter(body__contains=term)
        for i in p:
                html+='<h2>'+str(i)+'</h2>'+'<br/>'+i.body+'<br/>'
        return HttpResponse(html)
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 

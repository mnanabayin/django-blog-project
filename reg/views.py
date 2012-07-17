# Create your views here.

"""
Code that should be copy and pasted in to
reg/views.py to as a skeleton for creating
the authentication views
"""

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
	sess_comm = False
	if "uname_sess" in request.session:
		sess_comm = True
	disabled_accMsg = ''
	invalidMsg = ''
	sess_data = ''
	if "uname_sess" in request.session:
		sess_data = 'You are already logged in.'

	if request.method == 'POST':
    		uname = request.POST['username']	
		pword = request.POST['password']
		user = authenticate(username=uname, password=pword)
		if user is not None:
			if user.is_active:
				login(request, user)
				request.session["uname_sess"] = uname
				return HttpResponseRedirect('/blog/posts')
			
			##redirect
			else:
				disabled_accMsg = "Sorry, your account has been disabled. Contact the administrator."
				
			##return a disabled account msg
		else:
			invalidMsg = "Username or Password is invalid!"
			
		#return an invalid login message
	
	#YOUR CODE HERE
	else:
        	form = LoginForm()
	form = LoginForm()
	return render_to_response('reg/do_login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated(),
	'disabled_accMsg': disabled_accMsg,
	'invalidMsg': invalidMsg,
	'sess_data': sess_data,
	'sess_comm': sess_comm,
	'user': request.user
    })




@csrf_exempt
def do_logout(request):
	if "uname_sess" in request.session:
		del request.session["uname_sess"]
		logout(request)
		return render_to_response('reg/do_logout.html',{'l_out':True,'user': request.user})
	else:
		return HttpResponseRedirect("/reg/login")

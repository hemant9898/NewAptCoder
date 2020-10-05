from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
# Create your views here.


class RegisterFormT(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = User
    	fields = ["username", "email", "password1", "password2"]


class RegisterFormS(UserCreationForm):
	email = forms.EmailField()
	rolln = forms.IntegerField(label="roll_number")

	class Meta:
		model = User
		fields = ["rolln","email","username","password1", "password2"]



def index(request):
	if not request.user.is_authenticated: 
		return render(request,"aptcoder/home.html")
	else:
		if request.user.teacher.all():
			h = request.user.teacher.get()
			student = []
			for c in Course.objects.filter(teacher=h):
				temp = []
				temp.append(c.cname)
				for s in c.student.all():
					temp.append(s.Sname)
				student.append(temp)
			return render(request, "aptcoder/user.html",{
				"student": student,
				"user":request.user,
				"name":h.Tname,
				"course":Course.objects.filter(teacher=h),
				"non_course": Course.objects.exclude(teacher=h).all()
				})
		elif request.user.student.all():
			h=request.user.student.get()

			teacher = []
			for c in Course.objects.filter(student=h):
				temp=[]
				temp.append(c.cname)
				for t in c.teacher.all():
					temp.append(t.Tname)
				teacher.append(temp)

			return render(request,"aptcoder/sdash.html",{
				"teacher":teacher,
				"user":request.user,
				"name":h.Sname,
				"course":Course.objects.filter(student=h),
				"non_course":Course.objects.exclude(student=h).all()
				})
			



def login_view(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("aptcoder:index"))
		else:
			return render(request, "aptcoder/login.html",{
				"m": "Invalid"
				})
	return render(request,"aptcoder/login.html")

def logout_view(request):
	logout(request)
	return render(request, "aptcoder/login.html",{
				"m": "Logout"
				})


def register_teach(request):
	if request.method == "POST":
		form = RegisterFormT(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			tid=User.objects.get(username=username)
			teacher=Teacher(Tname=username,Tid=tid)
			teacher.save()
			return render(request, "aptcoder/login.html")
		else:
			return render(request, "aptcoder/register.html",{
				"form": form
				})

	return render(request, "aptcoder/register.html",{
				"form": RegisterFormT()
				})



	
def register_student(request):
	if request.method == "POST":
		form = RegisterFormS(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			rolln = form.cleaned_data["rolln"]
			sid=User.objects.get(username=username)
			student=Student(Sname=username,Sid=sid,rolln=rolln)
			student.save()
			return render(request, "aptcoder/login.html")
		else:
			return render(request, "aptcoder/reg_student.html",{
				"form": form
				})

	return render(request, "aptcoder/reg_student.html",{
				"form": RegisterFormS()
				})





def reg_course(request, userid):
	if request.method == "POST":
		teacher = Teacher.objects.get(Tid=userid)
		course = Course.objects.get(pk=int(request.POST["course"]))
		teacher.reg_course.add(course)

		student = []
		for c in Course.objects.filter(teacher=teacher):
			temp = []
			temp.append(c.cname)
			for s in c.student.all():
				temp.append(s.Sname)
			student.append(temp)

		return render(request, "aptcoder/user.html",{
					"student":student,
					"user":request.user,
					"name":teacher.Tname,
					"course":Course.objects.filter(teacher=teacher),
					"non_course": Course.objects.exclude(teacher=teacher).all(),
					})



def reg_courseSt(request, userid):
	if request.method == "POST":
		student = Student.objects.get(Sid=userid)
		course = Course.objects.get(pk=int(request.POST["course"]))
		student.reg_course.add(course)

		teacher = []
		for c in Course.objects.filter(student=student):
			temp=[]
			temp.append(c.cname)
			for t in c.teacher.all():
				temp.append(t.Tname)
			teacher.append(temp)

		return render(request, "aptcoder/sdash.html",{
					"teacher":teacher,
					"user":request.user,
					"name":student.Sname,
					"course":Course.objects.filter(student=student),
					"non_course": Course.objects.exclude(student=student).all(),
					})
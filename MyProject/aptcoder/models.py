from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Teacher(models.Model):
	Tname = models.CharField(max_length=30)
	Tid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")

	def __str__(self):
		return f"{self.id}: Teacher_name({self.Tname})"



class Student(models.Model):
	Sname = models.CharField(max_length=30)
	rolln = models.IntegerField()
	Sid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")

	def __str__(self):
		return f"{self.id}: student_roll_number({self.rolln}) Student_name({self.Sname})"


		

class Course(models.Model):
	cname = models.CharField(max_length=30)
	cid = models.IntegerField()
	teacher = models.ManyToManyField(Teacher, blank=True, related_name="reg_course")
	student = models.ManyToManyField(Student, blank=True, related_name="reg_course")


	def __str__(self):
		return f"{self.id}: course_id({self.cid}) course_name({self.cname})"











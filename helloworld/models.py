from django.db import models

# Create your models here.
class Klass(models.Model):
	"""docstring for Klass"""
	name = models.CharField('班级名称',max_length=20)
	note = models.TextField('班级介绍')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '班级'
		verbose_name_plural = verbose_name

class Student(models.Model):
	"""docstring for Student"""
	name = models.CharField('姓名', max_length=20)
	sex = models.CharField('性别', max_length=2)
	address = models.TextField('地址')
	klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='学生班级')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '学生'
		verbose_name_plural = verbose_name

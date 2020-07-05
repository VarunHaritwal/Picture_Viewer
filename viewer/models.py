from django.db import models

# Create your models here.
class Group(models.Model):
	group_name = models.CharField(max_length=120,null=True)
	date_created = models.DateTimeField(auto_now_add =False, null=True)

	def __str__(self):
		return (self.group_name)

class Question(models.Model):
	group_id = models.ForeignKey(Group,null=True, on_delete = models.CASCADE)
	question = models.FileField(null=True, blank=True)
	comment = models.CharField(max_length=200)
	created_at = models.CharField(null=True,max_length=200)

	def __str__(self):
		return (self.comment)
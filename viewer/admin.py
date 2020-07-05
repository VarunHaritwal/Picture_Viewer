from django.contrib import admin
from .models import Question, Group
# Register your models here.
class GroupModelAdmin(admin.ModelAdmin):
	list_display = ['__str__','date_created']
	class Meta:
		model = Group

class QuestionModelAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'comment', 'question','created_at']
	class Meta:
		model = Question


admin.site.register(Group, GroupModelAdmin)
admin.site.register(Question, QuestionModelAdmin)
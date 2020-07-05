from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Group, Question
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
	if request.user.is_authenticated:

		group_list = Group.objects.all()
		context = {
			'group_list' : group_list
		}
		return render(request, 'index.html', context)
	else:
		return Http404("Please Login to continue")

		
	
def detail(request, group_id):
    question_list = get_object_or_404(Group, pk=group_id)
    return render(request, 'detail.html', {'question_list': question_list})

def upload(request):
	if request.method =='POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name,uploaded_file)

	return render(request, 'base.html')   
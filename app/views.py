from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactUsForm, PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all()
    user = request.user
    context = {'posts': posts, 'user': user}
    return render(request, 'home.html', context)


@login_required
def create_post(request):
    context ={}
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Submitted Successfully.')
        else:
            return HttpResponse("Data Didn't Submit Successfully.")
    else:
        form = PostForm()
    context['form'] = form
    return render(request, "create-post.html", context)



 

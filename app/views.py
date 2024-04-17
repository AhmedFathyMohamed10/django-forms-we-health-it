from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactUsForm, PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


# Create your views here.
def posts(request):
    posts = Post.objects.all()
    user = request.user
    
    paginator = Paginator(posts, 5)  # Paginate by 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'user': user}
    return render(request, 'home.html', context)


def show_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'show_post.html', {'post': post})


@login_required
def display_posts(request):
    PostFormSet = formset_factory(PostForm, extra=0)
    posts = Post.objects.all()
    if request.method == 'POST':
        formset = PostFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('home')
    else:
        formset = PostFormSet(initial=[{'title': post.title, 'body': post.body} for post in posts])
    return render(request, 'display_posts.html', {'formset': formset})

@login_required
def create_post(request):
    context ={}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse("Data Didn't Submit Successfully.")
    else:
        form = PostForm()
    context['form'] = form
    return render(request, "create-post.html", context)


def custom_404(request, exception):
    return render(request, exception, '404.html', status=404)


def add_comment(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'show_post.html', {'form': form})

def show_comments(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    return render(request, 'show_post.html', {'comments': comments})

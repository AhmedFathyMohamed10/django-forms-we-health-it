from django import forms
from .models import Post, Comment

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Your name here', max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=11)
    message = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Title',
            'body': 'Body',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {'comment': 'Comment'}
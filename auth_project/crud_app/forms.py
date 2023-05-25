from django import forms
from .models import Blog, Comments


class BlogForm(forms.ModelForm):
    # tags = forms.CharField()

    class Meta:
        model = Blog
        fields = ('title', 'content', 'tags')
        labels = {
            'title': 'Blog Title',
            'content': 'Blog Content',
            'tags': 'Blog Tags'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the Blog Title Here'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter the blog content here, Minimum 50 Characters.'
            }),
            # 'tags': forms.TextInput(attrs={
            #     'placeholder': 'Provide the tags separated by space'
            # })
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment_text',)
        labels = {
            'comment_text': 'Comment Text'
        }
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Enter your Comment Here'
            })
        }


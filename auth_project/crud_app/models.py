from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class Tags(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.tag_name}'

    def get_absolute_url(self):
        return reverse('tag-details', kwargs={'pk': self.pk})


class Blog(models.Model):
    title = models.CharField(max_length=30, help_text='title should be descriptive')
    content = models.TextField(help_text='Should Contain at least 50 characters')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, related_name='blogs', help_text='Separate the tags using space')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog-details', kwargs={'pk': self.pk})


class Comments(models.Model):
    comment_text = models.TextField(help_text='Please add relative information about the Blog in the comment')
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.comment_text}'


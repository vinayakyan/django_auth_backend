# from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Tags
from .forms import BlogForm, CommentForm
from django.urls import reverse_lazy, reverse


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        user = self.request.user
        obj = form.save(commit=False)
        obj.created_by = user
        obj.save()
        for tag in tags.split():
            t, _ = Tags.objects.get_or_create(tag_name=tag.lower())
            obj.tags.add(t)
        obj.save()
        return super().form_valid(form)


class BlogDetails(LoginRequiredMixin, FormMixin, DetailView):
    model = Blog
    template_name = 'crud_app/blog_details.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(BlogDetails, self).get_context_data(**kwargs)
        context['form'] = CommentForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.blog = self.object
        obj.comment_by = self.request.user
        obj.save()
        return super(BlogDetails, self).form_valid(form)


class BlogList(LoginRequiredMixin, ListView):
    #model = Blog
    template_name = 'crud_app/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.all().order_by('-created_time')


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    #template_name = 'crud_app/blog_update.html'
    success_url = reverse_lazy('blogs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = "update"
        return context


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'crud_app/delete_confirm.html'
    success_url = reverse_lazy('blogs')


class TagDetails(DetailView):
    model = Tags
    template_name = 'crud_app/tags_details.html'

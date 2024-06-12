from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from news.models import Posts, PostComment
from .forms import AddPostForm, AddCommentForm
from pytils.translit import slugify
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class PostsListView(ListView):
    model = Posts
    context_object_name = 'posts'
    
    paginate_by = 3
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 6}
   
    
class PostDetailView(ModelFormMixin, DetailView):
    model = Posts
    form_class = AddCommentForm
    context_object_name = 'post'
    slug_url_kwarg = 'slug_id'
    
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Electronic Shop'
        context['cat_selected'] = 6
        context['comments'] = PostComment.objects.filter(post=kwargs['object'])
        
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = AddCommentForm(data=request.POST)
        
        if comment_form.is_valid():
            model = self.model.objects.get(slug=kwargs['slug_id'])
            comment_form = comment_form.save(commit=False)
            comment_form.post = model
            comment_form.user_name = self.request.user
            comment_form.save()
            model.comment_count += 1
            model.save()
            
            return redirect('news:post', comment_form.post.slug)

@method_decorator(never_cache, 'dispatch')
class AddPostCreateView(LoginRequiredMixin ,CreateView):
    model = Posts
    form_class = AddPostForm
    template_name = 'news/posts_form.html'
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 6}
    
    def form_valid(self, form):
        form.instance.name_user = self.request.user
        form.instance.slug = f'{slugify(form.instance.name_user)}-{slugify(form.instance.title)}'
        return super().form_valid(form)
    
  
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    context_object_name = 'post'
    form_class = AddPostForm
    slug_url_kwarg = 'slug_id'
    template_name = 'news/posts_form.html'
    extra_context = {'title': 'Electronic Shop', 'cat_selected': 6}
    
    def form_valid(self, form):
        form.instance.is_edit = True
        form.instance.time_edit = timezone.now()
        form.instance.slug = f'{slugify(form.instance.name_user)}-{slugify(form.instance.title)}'
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return self.request == obj.name_user


class DeletePostView(LoginRequiredMixin ,DeleteView):
    model = Posts
    context_object_name = 'post'
    slug_url_kwarg = 'slug_id'
    success_url = reverse_lazy('news:posts')
    
from django.views.generic import ListView

from news.models import Posts

# Create your views here.


class PostsListView(ListView):
    model = Posts
    context_object_name = 'posts'
    
    paginate_by = 3
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView

)
from .models import Post
from django.contrib.auth.models import User 
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): #get request --> list 

  template_name = "posts/list.html"

  model = Post

  context_object_name = "posts"

class PostDetailView(DetailView):
  template_name = "posts/detail.html"
  model = Post
  context_object_name = "single_post"


class PostCreateView(CreateView):
  template_name = "posts/new.html"
  model = Post

  fields = ["title","subtitle","body", "author"]

  def form_valid(self,form):
    form.instance.author = User.objects.last()
    return super().form_valid(form)


class PostUpdateView(UpdateView):
  template_name = "posts/edit.html"
  model = Post
  fields = ["title", "subtitle", "body"]
  success_url = reverse_lazy("post_list")





class PostDeleteView(DeleteView):
  template_name = "posts/delete.html"
  model = Post
  success_url = reverse_lazy("post_list")
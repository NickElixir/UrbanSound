from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Poster
from .forms import PosterForm

class HomeRendr(ListView):
    model = Poster
    template_name = 'home.html'

class MakePostView(CreateView):
    model = Poster
    form_class = PosterForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

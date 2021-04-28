from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Poster
from .forms import PosterForm
import os
import sys
sys.path.insert(1, '../')
import resnet_model_proc
from django.shortcuts import render

"""
class HomeRendr(ListView):
    model = Poster
    template_name = 'home.html'
"""

class MakePostView(CreateView):
    model = Poster
    form_class = PosterForm
    template_name = 'post.html'
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('print_pred')

def printer(request):
    data = dict()
    pred = resnet_model_proc.process_prediction()
        
    data = {
        'prediction' : pred,
    }

    return render(request, '../templates/pred.html', data)

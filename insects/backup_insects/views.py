from django.views.generic import ListView, DetailView
from .models import Insect

class InsectListView(ListView):
    model = Insect
    template_name = 'insects/insect_list.html'
    context_object_name = 'insects'

class InsectDetailView(DetailView):
    model = Insect
    template_name = 'insects/insect_detail.html'
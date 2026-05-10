from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Q
from .models import ContentOrder, ContentFamily, ContentSpecies

# LEVEL 0: Home
def home_view(request):
    suggestions = ContentOrder.objects.all()[:4]
    return render(request, 'insects/home.html', {'suggestions': suggestions})

# LEVEL 1: Orders List
def order_list_view(request):
    orders = ContentOrder.objects.all().order_by('name')
    return render(request, 'insects/order_list.html', {'orders': orders})

# LEVEL 2: Families List
def family_list_view(request, order_name):
    families = ContentFamily.objects.filter(order__name=order_name).order_by('name')
    return render(request, 'insects/family_list.html', {
        'order_name': order_name, 
        'families': families
    })

# LEVEL 3: Species Grid (FIXED: The definition line now matches!)
def species_grid_view(request, family_slug):
    family_obj = get_object_or_404(ContentFamily, slug=family_slug)
    species = ContentSpecies.objects.filter(family=family_obj)
    
    return render(request, 'insects/species_grid.html', {
        'family': family_obj,
        'species_list': species
    })

# LEVEL 4: Detail View
class InsectDetailView(DetailView):
    model = ContentSpecies
    template_name = 'insects/insect_detail.html'
    context_object_name = 'insect'

# LIVE SEARCH FUNCTION (FIXED: Now returns the new clean slugs!)
def live_search(request):
    query = request.GET.get('q', '')
    results = []
    if len(query) >= 2: 
        species = ContentSpecies.objects.filter(Q(common_name__icontains=query) | Q(scientific_name__icontains=query))[:5]
        for s in species:
            results.append({'name': s.common_name if s.common_name else s.scientific_name, 'type': 'Species', 'url': f'/insect/{s.slug}/'})

        families = ContentFamily.objects.filter(name__icontains=query)[:3]
        for f in families:
            results.append({'name': f.name, 'type': 'Family', 'url': f'/family/{f.slug}/'})
            
    return JsonResponse({'data': results})

# Error Pages
def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)
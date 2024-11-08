from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from ..models import Cover

class CoversListView(ListView):
    """
    View to display a list of all covers.
    """
    model = Cover
    template_name = 'cover_page.html'  # Specify your template name
    context_object_name = 'covers'  # Use this name in the template to access the list
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cover

def cover_page(request):
    covers = Cover.objects.all()
    context = {
        "cover": covers,
    }
    return render(request, 'cover_page.html', context)
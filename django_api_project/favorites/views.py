from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import FavoriteCharacter


@login_required
@require_POST
def toggle_favorite(request, character_id):
    name = request.POST.get('name')
    image_url = request.POST.get('image_url')

    favorite, created = FavoriteCharacter.objects.get_or_create(
        user=request.user,
        character_id=character_id,
        defaults={'name': name, 'image_url': image_url}
    )
    print(request)
    if not created:
        favorite.delete()
        messages.success(request, f"{name} removed from favorites.")
    else:
        messages.success(request, f"{name} added to favorites.")

    return redirect(request.META['HTTP_REFERER'])


@login_required
def dashboard(request):
    favorites = FavoriteCharacter.objects.filter(user=request.user)
    return render(request, 'favorites/dashboard.html', {'favorites': favorites})
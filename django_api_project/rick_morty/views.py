import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from favorites.models import FavoriteCharacter


@login_required(login_url='/accounts/login/')
def index(request):
    # Get the current page number from the query parameters, defaulting to 1
    page_number = request.GET.get('page', 1)
    search_query = {
        "name": request.GET.get('search.name', ''),
        "status": request.GET.get('search.status', ''),
        "species": request.GET.get('search.species', ''),
        "type": request.GET.get('search.type', ''),
        "gender": request.GET.get('search.gender', ''),
        "page": request.GET.get('search.page', '')}

    # Search for character or Fetch characters from the Rick and Morty API, specifying the page number
    search_query = {k: v for k, v in search_query.items() if v}

    url = f"https://rickandmortyapi.com/api/character/"
    try:
        # Make the API request
        response = requests.get(url, params=search_query)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        total_pages = data['info']['pages']
        page_range = list(range(1, total_pages + 1))

        if 'results' not in data or not data['results']:
            return JsonResponse({
                'error': 'No characters found matching the search criteria.',
                'results': [],
                'info': {'pages': 0}
            })
        else:
            characters = data['results']
        # Get the user's favorite characters
        favorite_ids = FavoriteCharacter.objects.filter(user=request.user).values_list('character_id', flat=True)

        # Add the is_favorite attribute to each character
        for character in data['results']:
            character['is_favorite'] = character['id'] in favorite_ids

        return render(request, 'rick_morty/index.html', {
            'characters': characters,
            'page_number': int(page_number),
            'total_pages': total_pages,
            'page_range': page_range,
            'search_query': search_query,
        })

    except requests.RequestException as e:
        # Handle any errors that occurred during the request
        return JsonResponse({
            'error': f'An error occurred while fetching data: {str(e)}',
            'results': [],
            'info': {'pages': 0}
        }, status=500)




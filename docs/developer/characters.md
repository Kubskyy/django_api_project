# Documentation: `index` View (Character Listing Page)

## Purpose

The `index` view serves as the main page where users can browse through the list of characters from the **Rick and Morty API**. It supports:
- Pagination
- Search functionality
- Indicating whether a character is marked as a favorite by the logged-in user.

## Prerequisites

- **Authentication**: The view is restricted to logged-in users. Unauthenticated users will be redirected to the login page (`/accounts/login/`).
- **Favorites Management**: Users can mark characters as favorites. Favorite character data is stored in the `FavoriteCharacter` model, associating characters with the logged-in user.

## URL Route

This view is linked to the **characters index page**, where all characters from the **Rick and Morty API** are listed.

## Core Functionality

### Query Parameters

The view processes multiple query parameters for pagination and search filters:

- **`page`**: Current page of the character list (defaults to 1).
- Search filters include:
    - `search.name`: Character’s name.
    - `search.status`: Character’s status (Alive, Dead, etc.).
    - `search.species`: Character’s species.
    - `search.type`: Character’s type.
    - `search.gender`: Character’s gender.

### API Call

The view interacts with the **Rick and Morty API** at `https://rickandmortyapi.com/api/character/`. It constructs the request dynamically based on the query parameters and fetches the results for:
- Pagination
- Search functionality
- Error handling if no results or a bad request occurs.

### Pagination

The API provides pagination information (`total_pages`), and the view computes the `page_range` for displaying pagination controls in the frontend.

### Favorites Handling

- The view checks the authenticated user’s favorite characters by querying the `FavoriteCharacter` model.
- Each character is tagged with an `is_favorite` attribute (`True` or `False`), indicating if it has been marked as a favorite by the current user.

### Error Handling

If the API request fails, an error message is returned via `JsonResponse`, along with a status code `500`.


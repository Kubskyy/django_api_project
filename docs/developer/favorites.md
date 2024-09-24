# Favorite Character Management Documentation

## Overview

This documentation covers the functionalities for managing favorite characters in a Django application, including the `FavoriteCharacter` model and the associated views: `toggle_favorite` and `dashboard`.

## Model: `FavoriteCharacter`

### Description
The `FavoriteCharacter` model stores the favorite characters of users, linking each user to a character via a unique ID, along with the character's name and image URL.

### Fields
- **user** (`ForeignKey` to `User`): The user associated with the favorite character.
- **character_id** (`IntegerField`): Unique identifier for the character.
- **name** (`CharField`): Name of the character.
- **image_url** (`URLField`): URL for the character's image.

### Meta
- **unique_together**: Ensures each user can only have one favorite for each character.

### String Representation
- Returns: `"{username}'s favorite: {character_name}"`

## Views

### `toggle_favorite`

Handles adding/removing characters from favorites based on character ID.

#### Parameters
- **request**: The HTTP request object with POST data.
- **character_id**: ID of the character to toggle.

#### Behavior
- Retrieves `name` and `image_url` from POST data.
- Uses `get_or_create`:
  - Deletes existing favorite and shows a success message if found.
  - Creates a new favorite and shows a success message if not found.
- Redirects to the referring page.

### `dashboard`

Renders the user's dashboard, displaying all favorite characters.

#### Parameters
- **request**: The HTTP request object.

#### Behavior
- Fetches favorites for the logged-in user.
- Renders `favorites/dashboard.html` with the list of favorites.

## Usage
- To toggle a favorite character, send a POST request to `toggle_favorite` with `character_id`, `name`, and `image_url`.
- Access the dashboard at the `dashboard` view.

## Requirements
- Users must be logged in to access both views (`@login_required`).
- `toggle_favorite` requires a POST request (`@require_POST`).

from django import template

from favorites.models import Favorite


register = template.Library()


@register.filter
def is_favorite(object, user):
    """
    Returns True, if object is already in user`s favorite list
    """
    if not user or not user.is_authenticated():
        return False
    return Favorite.objects.favorites_for_object(object, user).exists()

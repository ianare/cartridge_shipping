from django.http import JsonResponse
from .checkout import get_ship_choices


def get_choices(request, country):
    choices = get_ship_choices(country, request)
    if len(choices) > 1:
        choices.insert(0, {'code': '', 'display': ''})
    return JsonResponse({'choices': choices})

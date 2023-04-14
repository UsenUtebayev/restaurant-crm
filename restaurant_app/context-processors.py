from restaurant_app.models import Client


def get_role(request):
    try:
        role = Client.objects.get(pk=request.user.pk).role
    except Client.DoesNotExist:
        role = None
    return {'role': role}

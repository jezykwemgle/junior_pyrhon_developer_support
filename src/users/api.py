import json

from django.http import JsonResponse

from .models import User

# def all_users(request):
#     users = User.objects.all()
#     attrs = {"id", "email", "first_name", "last_name", "role"}
#     result: list[dict] = []
#
#     for user in users:
#         result.append({attr: getattr(user, attr) for attr in attrs})
#     return JsonResponse({"result": result})


def create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    user = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    attrs = {"id", "email", "first_name", "last_name", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)

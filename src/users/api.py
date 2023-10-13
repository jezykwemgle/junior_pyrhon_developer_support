import json

from django.http import JsonResponse

from .models import Issue, User


def all_users(request):
    users = User.objects.all()
    attrs = {"id", "email", "first_name", "last_name", "role"}
    result: list[dict] = []

    for user in users:
        result.append({attr: getattr(user, attr) for attr in attrs})
    return JsonResponse({"result": result})


def all_issues(request):
    issues = Issue.objects.all()
    attrs = {
        "id",
        "title",
        "body",
        "timestamp",
        "junior_id",
        "senior_id",
        "status",
    }

    result: list[dict] = []

    for issue in issues:
        result.append({attr: getattr(issue, attr) for attr in attrs})
    return JsonResponse({"result": result})


def create_user(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    user = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    attrs = {"id", "email", "first_name", "last_name", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)


def create_issue(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    issue = Issue.objects.create(**data)

    if not issue:
        raise Exception("Can not create issue")

    attrs = {
        "id",
        "title",
        "body",
        "timestamp",
        "junior_id",
        "senior_id",
        "status",
    }
    payload = {attr: getattr(issue, attr) for attr in attrs}
    return JsonResponse(payload)

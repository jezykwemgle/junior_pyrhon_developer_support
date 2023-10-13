import json

from django.http import JsonResponse

from issues.models import Issue

# def all_issues(request):
#     issues = Issue.objects.all()
#     attrs = {
#         "id",
#         "title",
#         "body",
#         "timestamp",
#         "junior_id",
#         "senior_id",
#         "status",
#     }
#
#     result: list[dict] = []
#
#     for issue in issues:
#         result.append({attr: getattr(issue, attr) for attr in attrs})
#     return JsonResponse({"result": result})


def create(request):
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

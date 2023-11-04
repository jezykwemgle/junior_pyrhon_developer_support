from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission

from issues.models import Issue
from users.constants import Role


class RoleIsJunior(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.JUNIOR

    def has_object_permission(self, request, api, issue):
        return request.user.role == Role.JUNIOR


class RoleIsSenior(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == Role.SENIOR

    def has_object_permission(self, request, api, issue):
        return request.user and request.user.role == Role.SENIOR


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == Role.ADMIN

    def has_object_permission(self, request, api, issue):
        return request.user and request.user.role == Role.ADMIN


class IsIssueParticipant(BasePermission):
    def has_object_permission(self, request, api, issue):
        return request.user and (
            request.user == issue.junior or request.user == issue.senior
        )


class CanCreateMessages(BasePermission):
    def has_permission(self, request, view):
        try:
            issue = Issue.objects.get(
                id=request.parser_context["kwargs"]["issue_id"]
            )
            return IsIssueParticipant().has_object_permission(
                request, view, issue
            )
        except Issue.DoesNotExist:
            raise NotFound("Issue not found")

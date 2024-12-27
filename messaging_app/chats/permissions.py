from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user in obj.participants.all():
            return True
        return False

from django_filters import rest_framework as filters
from .models import Message


class MessageFilter(filters.FilterSet):
    sender = filters.CharFilter(
        field_name="sender__username", lookup_expr="icontains"
    )

    sent_after = filters.DateTimeFilter(
        field_name="sent_at", lookup_expr="gte"
    )

    sent_before = filters.DateTimeFilter(
        field_name="sent_at", lookup_expr="lte"
    )

    conversation_id = filters.UUIDFilter(
        field_name="conversation__conversation_id"
    )

    class Meta:
        model = Message
        fields = ["sender", "sent_after", "sent_before", "conversation_id"]

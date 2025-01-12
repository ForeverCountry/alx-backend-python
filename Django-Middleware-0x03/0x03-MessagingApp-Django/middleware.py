import datetime
import logging
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename="requests.log", level=logging.INFO, format="%(message)s"
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = (
            f"{datetime.datetime.now()} - User: {user} - Path: {request.path}"
        )

        logging.info(log_message)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_reponse):
        self.get_response = get_reponse

    def __call__(self, request):
        current = datetime.datetime.now().hour

        if current < 9 or current >= 18:
            return HttpResponseForbidden(
                "Access to the messaging app outside 9 AM to 6 PM"
            )
        response = self.get_response(request)
        return response

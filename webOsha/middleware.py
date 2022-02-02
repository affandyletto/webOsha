from django.http import HttpResponsePermanentRedirect


class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(':')[0]
        if host == "lskosha.co.id":
            return HttpResponsePermanentRedirect(
                "https://www.lskosha.co.id/" + request.path
            )
        else:
            return self.get_response(request)
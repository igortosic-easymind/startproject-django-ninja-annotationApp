from django.core.cache import cache
from django.http import HttpResponse


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        key = f"rate_limit_{ip}"
        if cache.get(key, 0) >= 100:  # 100 requests per minute
            return HttpResponse("Rate limit exceeded", status=429)
        cache.set(key, cache.get(key, 0) + 1, 60)  # 60 seconds expiry
        return self.get_response(request)

from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.http import HttpResponse
from functools import wraps
from django.shortcuts import render


def curator_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Curator').exists():
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapper

def rate_limiter(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            ip = request.META.get('REMOTE_ADDR')
            key = f"rate_limit_{ip}"
            attempts = cache.get(key, 0)

            if attempts >= 5:
                return render(request, 'pages/login.html', {
                    'form' : None,
                    'error': "Too many login attempts. Please try again later.",
                    'locked': True
                })
            
            response = view_func(request, *args, **kwargs)

            if response.status_code == 302:
                cache.delete(key)
            else:
                cache.set(key, attempts + 1, timeout = 60)

            return response
        return view_func(request, *args, **kwargs)
    return wrapper
        
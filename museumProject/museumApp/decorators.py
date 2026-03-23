from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.http import HttpResponse
from functools import wraps
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse


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
        
def paginator(q_set_key, per_page=9):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)

            if not isinstance(response, TemplateResponse):
                return response
            
            q_set = response.context_data.get(q_set_key)
            if q_set is None:
                return response
            
            page_num = request.GET.get('page', 1)
            paginator = Paginator(q_set, per_page)

            try:
                page = paginator.page(page_num)
            except (PageNotAnInteger, EmptyPage):
                page = paginator.page(1)

            response.context_data[q_set_key] = page.object_list
            response.context_data['page'] = page
            response.context_data['paginator'] = paginator

            return response
        return wrapper
    return decorator

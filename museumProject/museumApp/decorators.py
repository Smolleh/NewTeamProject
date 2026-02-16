from django.http import HttpResponseForbidden

def curator_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='Curator').exists():
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapper


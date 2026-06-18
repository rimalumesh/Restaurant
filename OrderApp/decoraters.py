from functools import wraps
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(roles):
    def decorater(view_func):
        @wraps(view_func)
        def _wraped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login_view_url')
            
            if request.user.role not in roles:
                raise PermissionDenied ("Access denied.")
            return view_func(request, *args, **kwargs)
        return _wraped_view
    return decorater
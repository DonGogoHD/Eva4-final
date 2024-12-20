from django.shortcuts import redirect

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('index') 
        return view_func(request, *args, **kwargs)
    return _wrapped_view

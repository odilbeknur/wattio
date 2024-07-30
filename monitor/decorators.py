from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'access_token' not in request.session:
            return redirect('login')  # Redirect to login page if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper

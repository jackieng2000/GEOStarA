# account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, 'You are now logged in!')
#             return redirect('index')  # Redirect to home or another page
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

# def user_logout(request):
#     if request.method == 'POST':
#         logout(request)
#         messages.success(request, 'You have been logged out.')
#         return redirect('pages:index')  # Or 'login'
#     return redirect('pages:index')


from accounts.utils import is_google_user, get_social_provider

def user_profile(request):
    user = request.user
    context = {
        'is_google_user': is_google_user(user),
        'social_provider': get_social_provider(user),
    }
    return render(request, 'profile.html', context)

def admin_dashboard(request):
    from django.contrib.auth.models import User
    from accounts.utils import is_google_user
    
    users = User.objects.all()
    user_stats = []
    
    for user in users:
        user_stats.append({
            'username': user.username,
            'email': user.email,
            'is_google_user': is_google_user(user),
            'provider': get_social_provider(user),
        })
    
    context = {'user_stats': user_stats}
    return render(request, 'admin_dashboard.html', context)



from django.contrib.auth.decorators import login_required
from .utils import is_google_user, get_social_provider

@login_required
def registration_info(request):
    """
    Display user's registration information
    """
    user = request.user
    context = {
        'is_google_user': is_google_user(user),
        'social_provider': get_social_provider(user),
        'registration_method': get_user_registration_method(user),
    }
    return render(request, 'accounts/registration_info.html', context)

from django.views.generic import TemplateView

class EmailConfHelpView(TemplateView):
    template_name = 'account/email_confirmation_help.html'


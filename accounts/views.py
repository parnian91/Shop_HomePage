from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    next_page = request.GET.get('next', '/')
                    print('Log:',next_page)
                    messages.success(request,'Login successful')
                    return redirect(next_page)
                
                        # Return an 'invalid login' error message.
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')  

@login_required(login_url="/accounts/login")
def logout_view(request):
    logout(request)
    messages.success(request,'Logout successful')
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)  
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password1 = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password1)
                login(request, user)
                messages.success(request,'Account created successfully')
                return redirect('/')
        form = UserCreationForm()  
        context = {'form':form}  
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
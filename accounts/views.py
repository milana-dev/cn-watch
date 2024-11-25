from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
# Create your views here.

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Ugurla daxil oldunuz,{user.username}')
            return redirect('all_watches')
        else:
            messages.info(request, 'Istifadeci adi ve ya parol yanlisdir!')

    form = AuthenticationForm()
    return render(request, 'accounts_temp/login.html', {'form':form})
    



def sign_out(request):
    logout(request)
    return redirect('all_watches')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_watches')
            else:
                return render(request, 'accounts_temp/register.html', {'form':form})
        else:
            if form.errors.get('password2'):
                form.add_error('password2', 'Parollar uygun deyil.Lutfen yeniden daxil edin')
            return render(request, 'accounts_temp/register.html', {'form':form})

    else:
        form = UserCreationForm()

    return render(request, 'accounts_temp/register.html', {'form':form})



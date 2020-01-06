from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:

            if not (User.objects.filter(username = username).exists()):
                if not (User.objects.filter(email = email).exists()):
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
                    
                else:
                    messages.info(request,'email already exists')
                    return redirect('register')

            else:
                messages.info(request,"user already exists")
                return redirect('register')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')

    
    else:           #Get request
        return render(request, 'register.html', )


def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"invalid credendials")
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






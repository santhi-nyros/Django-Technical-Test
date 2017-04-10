from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Import the built-in password reset view and password reset confirmation view.
from django.contrib.auth.views import password_reset

from .forms import *
from .models import UserProfle,Todos
# Create your views here.


#User registration
def regisration(request):
    form = RegistrationForm()
    if request.method == 'POST': # Post method
        username = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        data = request.POST
        try :
            # checking for new user or existed user
            user = User.objects.get(email=email)
            status = 'User alredy existed with this mails.Please go with login.'
        except User.DoesNotExist :
            # if new user save the details in database
            user = User()
            user.username = username
            user.first_name = f_name
            user.last_name = l_name
            user.email = email
            user.set_password(password)
            user.save()
            uprof = UserProfle()
            uprof.user = user
            uprof.address = address
            uprof.save()
            status = 'User succesfully registrated, please go with login page.'
        return render(request,'registration.html',{"form":form,'status':status})
    # if Get method
    return render(request,'registration.html',{"form":form})



#User Login
def login(request):
    form = LoginForm()
    if request.method =='POST':# POST method
        email = request.POST['email']
        password = request.POST['password']
        try:
            #if user is existed or not
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user) # login the user
                    return HttpResponseRedirect('/')
            else:
                status = "The email or password you have entered is invalid!"
        except User.DoesNotExist :
            status = "User does not existed with this mail, please go with registration page."
        return render(request,'login.html',{"form":form,"status":status})
    # Get method
    return render(request,'login.html',{"form":form})


# Logout
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# Updating user details
@login_required
def updateProfile(request):
    user = User.objects.get(email = request.user.email)
    u_profile = UserProfle.objects.get(user = user)
    form = EditForm(initial={'username': user, 'first_name':user.first_name,'last_name':user.last_name,'address':u_profile.address})
    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        u_profile.address = request.POST['address']
        u_profile.save()
        return HttpResponseRedirect('/accounts/update/')
    return render(request,'update.html',{"form":form})


# authenticated user password reset
@login_required
def password_reset(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        if (request.POST['password'] == request.POST['password_confirm']):
            user = User.objects.get(email = request.user.email)
            user.set_password(request.POST['password'])
            user.save()
            return HttpResponseRedirect("/accounts/login/")
        return render(request,'reset_password.html',{"form":form ,'status':'Password mismatched,please try again.'})
    return render(request,'reset_password.html',{"form":form})




class todos_view(View):
    template_name = 'todos.html'
    form_class = TodoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(todos_view, self).dispatch(*args, **kwargs)

    def get(self, request,*args, **kwargs):
        todos = Todos.objects.all()
        return render(request, self.template_name, {'todos': todos})



class AddTaskView(View):
    template_name = 'todos.html'
    form_class = TodoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddTaskView, self).dispatch(*args, **kwargs)

    def get(self, request,*args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            task.user = request.user # Set the user object here
            task.save()
            return HttpResponseRedirect('/accounts/todos/')



@login_required
def UpdateTodo(request,pk):
    todo = Todos.objects.get(id = pk)
    data = {'name':todo.name, 'description':todo.description, 'status':todo.status}

    form = TodoEditForm(data=request.POST or None)
    if request.method == 'POST':
        print request.POST
        todo.name = request.POST['name']
        todo.description = request.POST['description']
        todo.status = request.POST['status']
        todo.save()
        return HttpResponseRedirect('/accounts/todos/')


    form = TodoEditForm(initial=data)

    return render(request,'updatetodo.html',{"form":form})


@login_required
def DeleteTodo(request,pk):
    todo = Todos.objects.get(id = pk).delete()
    return HttpResponseRedirect('/accounts/todos/')

@login_required
def ChangeTodoStatus(request,pk):
    if request.method == 'POST':
        print request.POST
        todo = Todos.objects.get(id = pk)
        todo.done_by = request.POST['didUser']
        todo.status = 'True'
        todo.save()
    return HttpResponseRedirect('/accounts/todos/')

@login_required
def HideTodos(request):
    todos = Todos.objects.filter(status = False)
    return render(request, 'todos.html', {'todos': todos})

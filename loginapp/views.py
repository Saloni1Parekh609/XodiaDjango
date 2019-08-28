from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Profile, User
from django.views.generic import View
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError



class Register(View):
    template_name= 'loginapp/register.html'

    def get(self,request):
        return render(request, self.template_name)

class Success(View):
    template_name= 'loginapp/success.html'

    def get(self,request):
        if not request.user.is_authenticated():
            return redirect(reverse('game:login'))
        user = request.user.username
        context = {
            'username': user
        }
        return render(request, self.template_name,context)

class Fail(View):
    template_name= 'loginapp/fail.html'

    def get(self,request):
        return render(request, self.template_name)

class SubmitView(View):

    template_name='loginapp/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        user=User()
        name=request.POST.get("username")
        email=request.POST.get("email")
        psw=request.POST.get("password")
        #user = User.objects.create_user(username=name, password=psw, email=email)
        #user.save()


        user.username = name
        user.set_password(psw)

        user.email = email

        if name != "" and psw != "":
            try:
                user.save()

            except IntegrityError:
                context={
                    'IntegrityError': 'Username exists'
                }
                return render(request, 'loginapp/signup.html', context)
        else:
            return render(request, 'loginapp/signup.html')

        profile = Profile()
        profile.user = user
        #profile.is_active= True
        profile.save()
        context = {
            'username': user.username
        }

        return render(request, 'loginapp/success.html',context)



class LoginView(View):
    template_name='loginapp/login.html'

    def get(self, request):

        def get(self, request):
            if request.user.is_authenticated():
                user = request.user.username
                context = {
                    'username': user
                }
                return render(request, 'loginapp/success.html', context)
            else:
                return render(request, self.template_name)
            """try:
                LogIn = Profile.objects.get(is_active=True)
                return render(request, 'loginapp/success.html', {"profiles": LogIn})
            except ObjectDoesNotExist:
                return render(request, self.template_name)"""

    def post(self,request):
        name=request.POST.get("username")
        psw=request.POST.get("password")
        user = authenticate(username=name, password=psw)
        if user is not None:
            """active = Profile.objects.get(user__username=request.user.username)
            active.is_active = True
            active.save()"""
            context = {
                'username': user.username
            }
            return render(request, 'loginapp/success.html', context)
        else:
            context = {
                'LoginError': "Username/Password incorrect"
            }
            return render(request, "loginapp/login.html", context)
            #return render(request, 'loginapp/success.html',{"profiles": active})
        """else:
            return render(request, "loginapp/login.html")"""






# Create your views here.

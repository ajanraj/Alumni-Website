from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login as auth_login
from homepage.models import CustomUser as User
import re
# Create your frontend here.


def index(request):
    return render(request, 'frontend/index.html')


@login_required(login_url='frontend.login')
def profile(request):
    user = User.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "Login to Continue!")
        return redirect('frontend.index')

    else:
        user = user.get()

    return render(request, 'frontend/profile.html', {'user': user})


@login_required(login_url='frontend.login')
def edit_profile(request):
    user = User.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "Login to Continue!")
        return redirect('frontend.index')

    else:
        user = user.get()

    return render(request, 'frontend/edit_profile.html', {'user': user})


@login_required(login_url='frontend.login')
def update(request):
    if request.method == "POST":
        user = User.objects.filter(pk=request.user.id)

        if not user:
            messages.error(request, "Login to Continue!")
            return redirect('frontend.index')

        else:
            user = user.get()

        if not 'firstname' in request.POST.keys():
            messages.error(request, "FirstName is missing")
            return redirect("frontend.signup")

        if not 'lastname' in request.POST.keys():
            messages.error(request, "LastName is missing")
            return redirect("frontend.signup")

        if not 'username' in request.POST.keys():
            messages.error(request, "Name is missing")
            return redirect("frontend.signup")

        if not 'email' in request.POST.keys():
            messages.error(request, "Email is missing")
            return redirect("frontend.signup")

        if not 'number' in request.POST.keys():
            messages.error(request, "Number is missing")
            return redirect("frontend.signup")

        if not 'working_organization' in request.POST.keys():
            messages.error(request, "Working Organization is missing")
            return redirect("frontend.signup")

        if not 'domain' in request.POST.keys():
            messages.error(request, "Domain is missing")
            return redirect("frontend.signup")

        if not 'designation' in request.POST.keys():
            messages.error(request, "Designation is missing")
            return redirect("frontend.signup")

        if not 'skill_sets' in request.POST.keys():
            messages.error(request, "Skill Sets is missing")
            return redirect("frontend.signup")

        # if not 'gender' in request.POST.keys():
        #     messages.error(request, "Gender is missing")
        #     return redirect("frontend.signup")

        if not 'password' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.signup")

        if not 're_pass' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.signup")

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        working_organization = request.POST['working_organization']
        domain = request.POST['domain']
        designation = request.POST['designation']
        skill_sets = request.POST['skill_sets']
        # gender = request.POST['gender']
        password = request.POST['password']
        re_pass = request.POST['re_pass']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', username):
            messages.error(request, "Enter a valid name!")
            return redirect("frontend.signup")
        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", email):
            messages.error(request, "Enter a valid Email!")
            return redirect('frontend.signup')
        if len(password) < 4:
            messages.error(request, "Password is Too Short")
            return redirect('frontend.signup')
        if password != re_pass:
            messages.error(request, "Repeat the password correctly")
            return redirect('frontend.signup')
        if not re.match('^[\d]{10,12}$', number):
            messages.error(request, "Invalid Phone number")
            return redirect('frontend.signup')
        # if gender == "-1":
        #     messages.error(request, "Select a gender")
        #     return redirect("frontend.signup")

        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.phone = number
        user.working_organization = working_organization
        user.domain = domain
        user.designation = designation
        skill_sets = skill_sets
        user.password = make_password(password)

        user.save()

        messages.success(request, "Profile Updated")
        return redirect("frontend.profile")

    else:
        return redirect("frontend.edit_profile")


def signup(request):
    if request.method == "POST":
        if not 'firstname' in request.POST.keys():
            messages.error(request, "FirstName is missing")
            return redirect("frontend.signup")

        if not 'lastname' in request.POST.keys():
            messages.error(request, "LastName is missing")
            return redirect("frontend.signup")

        if not 'username' in request.POST.keys():
            messages.error(request, "Name is missing")
            return redirect("frontend.signup")

        if not 'email' in request.POST.keys():
            messages.error(request, "Email is missing")
            return redirect("frontend.signup")

        if not 'number' in request.POST.keys():
            messages.error(request, "Number is missing")
            return redirect("frontend.signup")

        if not 'working_organization' in request.POST.keys():
            messages.error(request, "Working Organization is missing")
            return redirect("frontend.signup")

        if not 'domain' in request.POST.keys():
            messages.error(request, "Domain is missing")
            return redirect("frontend.signup")

        if not 'designation' in request.POST.keys():
            messages.error(request, "Designation is missing")
            return redirect("frontend.signup")

        if not 'skill_sets' in request.POST.keys():
            messages.error(request, "Skill Sets is missing")
            return redirect("frontend.signup")

        # if not 'gender' in request.POST.keys():
        #     messages.error(request, "Gender is missing")
        #     return redirect("frontend.signup")

        if not 'password' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.signup")

        if not 're_pass' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.signup")

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        working_organization = request.POST['working_organization']
        domain = request.POST['domain']
        designation = request.POST['designation']
        skill_sets = request.POST['skill_sets']
        # gender = request.POST['gender']
        password = request.POST['password']
        re_pass = request.POST['re_pass']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', username):
            messages.error(request, "Enter a valid name!")
            return redirect("frontend.signup")
        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", email):
            messages.error(request, "Enter a valid Email!")
            return redirect('frontend.signup')
        if len(password) < 4:
            messages.error(request, "Password is Too Short")
            return redirect('frontend.signup')
        if password != re_pass:
            messages.error(request, "Repeat the password correctly")
            return redirect('frontend.signup')
        if not re.match('^[\d]{10,12}$', number):
            messages.error(request, "Invalid Phone number")
            return redirect('frontend.signup')
        # if gender == "-1":
        #     messages.error(request, "Select a gender")
        #     return redirect("frontend.signup")

        try:
            signup = User(username=username, email=email, first_name=firstname, last_name=lastname, phone=number,
                          working_organization=working_organization, domain=domain, designation=designation, skill_sets=skill_sets)
            signup.set_password(password)
            signup.save()
        except Exception as e:
            messages.success(
                request, e)
            return redirect("frontend.signup")

        messages.success(request, "Signed up successfully")
        return redirect("frontend.login")

    else:
        # return redirect("admin.song.add")
        return render(request, 'frontend/signup.html')


def contact(request):
    if request.method == "POST":
        # do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send Email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['anishooty2016@gmail.com'],  # to email
            fail_silently=False,
        )

        return render(request, 'frontend/contact.html', {'message_name': message_name})

    else:
        # return the page
        return render(request, 'frontend/contact.html', {})


def login(request):
    return render(request, 'frontend/login.html', {})


def login_post(request):
    if request.method == "POST":
        if not 'email' in request.POST.keys():
            messages.error(request, "Email is missing")
            return redirect("frontend.login")

        if not 'password' in request.POST.keys():
            messages.error(request, "Password is missing")
            return redirect("frontend.login")

        email = request.POST['email']
        password = request.POST['password']

        if not re.match(r"^[\w\.\+\-\_]+\@[\w-]+\.[a-z]{2,3}$", email):
            messages.error(request, "Enter a valid Email!")
            return redirect('frontend.login')
        if len(password) < 4:
            messages.error(request, "Password is Too Short")
            return redirect('frontend.login')

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=email)

            if user.check_password(password):
                auth_login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('frontend.index')
            else:
                messages.error(request, "Invalid Password")
                return redirect('frontend.login')

        except UserModel.DoesNotExist:
            messages.error(request, "Invalid Email Please Register !")
            return redirect('frontend.login')
    else:
        messages.error(request, "Invalid Token")
        return redirect('frontend.login')


@login_required(login_url='frontend.login')
def logout_post(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('frontend.index')


def admin(request):
    return render(request, 'admin.html', {})


def forum(request):
    return render(request, 'forum.html', {})


def register(response):
    form = UserCreationForm()
    return render(response, "templates/register.html", {"form": form})

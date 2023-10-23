from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profil, Skill
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomProfilCreationForm, SkillForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def profiles(request):
    users = Profil.objects.exclude(user__username="admin")
    q = request.GET.get("q")
    if q:
        users = Profil.objects.filter(
            Q(name__icontains=q)
            | Q(email__icontains=q)
            | Q(user__username__icontains=q)
            | Q(user__first_name__icontains=q)
            | Q(user__last_name__icontains=q)
        )

    p = Paginator(users, 9)
    page = request.GET.get("page")
    user = p.get_page(page)
    context = {
        "users": users,
        "pagination": user,
        "nums": "s" * p.num_pages,
        "query": q,
    }

    return render(request, "user_templates/profiles.html", context)


def get_profile(request, id):
    user = Profil.objects.get(id=id)
    context = {"user": user}
    return render(request, "user_templates/profile.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga hush kelibsiz ✅")
            return redirect("profiles")
        else:
            messages.error(request, "Bunday login va parol mavjud emas ❌")

    else:
        return render(request, "user_templates/login.html")


def logout_user(request):
    logout(request)
    messages.warning(request, "Tizimdan chiqdingiz ❌")
    return redirect("login_user")


def register_user(request):
    form = CustomUserCreationForm()
    for f in form:
        if f.label == "Password":
            f.label = "Parol"
        elif f.label == "Password confirmation":
            f.label = "Parolni tasdiqlang"

    context = {"form": form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz ✅")
            return redirect("profiles")
        else:
            messages.error(request, "Ro'yxatdan o'tmadingiz ❌")

    return render(request, "user_templates/register_user.html", context)


@login_required(login_url="login_user")
def account(request):
    profil = request.user.profil
    context = {"profil": profil}
    return render(request, "user_templates/account.html", context)


@login_required(login_url="login_user")
def account_edit(request):
    profil = request.user.profil
    form = CustomProfilCreationForm(instance=profil)
    if request.method == "POST":
        form = CustomProfilCreationForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar muvaffaqiyatli o'zgartirildi ✅")
            return redirect("my_account")

    context = {"form": form}
    return render(request, "user_templates/account_edit.html", context)


@login_required(login_url="login_user")
def add_malaka(request):
    user = request.user
    profil = get_object_or_404(Profil, user=user)
    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = profil
            skill.save()
            messages.success(request, "Malaka muvaffaqiyatli qo'shildi ✅")
            return redirect("my_account")

    else:
        form = SkillForm()

    context = {"form": form}
    return render(request, "user_templates/add_malaka.html", context)


@login_required(login_url="login_user")
def edit_malaka(request, id):
    skill = Skill.objects.get(id=id)
    form = SkillForm(instance=skill)
    profil = get_object_or_404(Profil, user=request.user)
    try:
        if request.method == "POST":
            form = SkillForm(request.POST, instance=skill)
            if form.is_valid():
                skill = form.save(commit=False)
                skill.user = profil
                form.save()
                messages.success(request, "Malaka muvaffaqiyatli o'zgartirildi ✅")
                return redirect("my_account")

        form = SkillForm(instance=skill)
        context = {"form": form, "skill": skill}

        return render(request, "user_templates/edit_malaka.html", context)

    except Skill.DoesNotExist:
        messages.error(
            request, "Siz faqat o'zingizga tegishli malakani o'zgartira olasiz ❌"
        )
        return redirect("my_account")


@login_required(login_url="login_user")
def delete_malaka(request, id):
    skill = Skill.objects.get(id=id)
    try:
        if str(skill.user.user.username) == str(request.user) or request.user.is_staff:
            skill.delete()
            messages.success(request, "Malaka o'chirildi ✅")
            return redirect("my_account")
        else:
            messages.warning(
                request, "Siz faqat o'zingizga tegishli malakani o'chira olasiz ❌"
            )

    except Skill.DoesNotExist:
        messages.warning(request, "Bunday malaka mavjud emas ❌")
        return redirect("my_account")

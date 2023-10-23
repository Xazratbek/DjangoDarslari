from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Comment
from .forms import ProjectForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def projects(request):
    projects = Project.objects.all()
    q = request.GET.get("q")

    if q:
        projects = projects.filter(Q(title__icontains=q) | Q(description__icontains=q))

    p = Paginator(projects, 9)
    page = request.GET.get("page")
    project = p.get_page(page)

    context = {
        "projects": projects,
        "pagination": project,
        "nums": "s" * p.num_pages,
        "query": q,
    }
    return render(
        request,
        "project/projects.html",
        context,
    )


def get_project(request, id):
    project = get_object_or_404(Project, id=id)
    comments = Comment.objects.filter(project=project)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.comment_user = request.user.profil
            comment.text = request.POST["message"]
            if len(comment.text) == 0:
                messages.warning(
                    request, "Bo'sh matn bilan comment qoldirib bo'lmaydi ❌"
                )
                return redirect("project", id=id)
            else:
                comment.save()
                messages.success(request, "Comment qo'shildi ✅")
                return redirect("project", id=id)
    else:
        form = CommentForm()

    context = {
        "project": project,
        "comments": comments,
        "form": form,
    }

    return render(request, "project/project.html", context=context)


@login_required(login_url="login_user")
def project_add(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profil
            project.save()
            messages.success(request, f"{project.title} loyihasi qo'shildi ✅")
            return redirect("projects")

    form = ProjectForm()

    context = {"form": form}
    return render(request, "project/project_add.html", context)


def edit_project(request, id):
    profil = request.user.profil
    try:
        project = profil.project_set.get(id=id)
        form = ProjectForm(instance=project)
        print(form)
        if request.method == "POST":
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                messages.success(request, "Loyiha ma'lumotlari o'zgartirildi ✅")
                return redirect("projects")

        context = {"form": form}

        return render(request, "project/project_add.html", context)

    except Project.DoesNotExist:
        messages.warning(
            request, "Siz faqat o'zingizga tegishli loyihani o'zgartirishingiz mumkin ❌"
        )
        return redirect("my_account")


@login_required(login_url="login_user")
def delete_project(request, id):
    profil = request.user.profil
    try:
        project = profil.project_set.get(id=id)
        project.delete()
        messages.warning(request, f"{project.title} loyihasi o'chirib tashlandi ✅")
        return redirect("projects")

    except Project.DoesNotExist:
        messages.warning(
            request, "Siz faqat o'zingizga tegishli loyihani o'chirishingiz mumkin ❌"
        )
        return redirect("my_account")


@login_required(login_url="login_user")
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if (
        request.user.username == comment.comment_user.user.username
        or request.user.is_staff
    ):
        comment.delete()
        messages.success(request, "Comment o'chirildi ✅")
        return redirect("project", id=comment.project.id)

    else:
        messages.error(
            request, "Siz faqat o'zingizga tegishli commentni o'chira olasiz ❌"
        )
        return redirect("project", id=comment.project.id)

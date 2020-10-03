# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from datetime import datetime

from .models import UserProfile
from authentication.models import Chapter
from .forms import UserProfileForm
from website.models import Announcement


@login_required(login_url="/login/")
def index(request):
    context = {"chapters": Chapter.objects.all(), "announcements": Announcement.objects.all()}
    return render(request, "index.html", context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split("/")[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template("error-404.html")
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template("error-500.html")
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile_create_view(request):
    context = {}
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    context['profile'] = profile

    if request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            # profile.chapter = request.user.chapter.all
            if request.FILES:
                profile.profile_picture = request.FILES["profile_picture"]
            else:
                profile.profile_picture = profile.profile_picture
            # profile.date_joined = datetime.now()
            # profile.last_login = datetime.now()
            if profile.dob and profile.field_of_study and profile.bio and profile.status and profile.skills:
                profile.is_complete = True
            profile.save() 
            return redirect("profile")
        else:
            context["profile_form"] = form
    else:
        form = UserProfileForm(
            initial={
                # 'first_name': profile.first_name,
                # 'last_name': profile.last_name,
                "dob": profile.dob,
                # 'gender': profile.gender,
                # 'occupational_status': profile.occupational_status,
                "field_of_study": profile.field_of_study,
                # 'chapter': profile.chapter.all,
                # 'country': profile.country,
                "bio": profile.bio,
                "status": profile.status,
                "skills": profile.skills,
                "fb_link": profile.fb_link,
                "tw_link": profile.tw_link,
                "ig_link": profile.ig_link,                
                "profile_picture": profile.profile_picture,
            }
        )

        context["profile_form"] = form

    return render(request, "accounts/create-profile.html", context)


@login_required(login_url="/login/")
def profile_view(request):
    context = {}
    # print(request.user.chapter)
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    context["profile"] = profile
    context["user"] = request.user
    return render(request, "accounts/profile.html", context)

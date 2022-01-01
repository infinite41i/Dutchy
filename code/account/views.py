import json

from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from dong_yab.settings import MEDIA_ROOT
from .models import *
# Create your views here.
from django.urls import reverse
from django.db.models import Sum, F, Subquery, OuterRef, Count
from sendfile import sendfile

from account.forms import RegisterForm, LoginForm


def first_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home", kwargs={"uuid": "1"}))
    return HttpResponseRedirect(reverse("sign"))


def sign(request):
    if request.method == "GET":
        return render(request, 'sign.html', {"error": ""})
    else:
        if "register" in request.POST:
            form = RegisterForm(request.POST)
            if not form.is_valid():
                return render(request, 'sign.html', {"error": form.errors})
            form.save()
            return HttpResponseRedirect(reverse("sign"))
        elif "login" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(username=form.cleaned_data["username"]).first()
                valid = user.check_password(form.cleaned_data["password"]) if user else False
                if valid:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home", kwargs={"uuid": "1"}))
                else:
                    return render(request, 'sign.html', {"error": "نام کاربری یا رمز عبور اشتباه است"})
            return render(request, 'sign.html', {"error": form.errors})

    return HttpResponse()


def add_balance(request):
    profile = request.user.profile
    profile.wallet += int(request.GET.get("price", 0))
    profile.save()
    return HttpResponseRedirect(reverse("home", kwargs={"uuid": "1"}))


def add_group(request):
    group = Group(name=request.POST.get("name_group"), description=request.POST.get("description"), uuid=uuid.uuid4(),
                  image=request.FILES.get("file", None))
    group.save()
    group.group_members.add(request.user)
    group.save()
    return HttpResponseRedirect(reverse("home", kwargs={"uuid": "1"}))


def join_group(request):
    user = request.user
    group = Group.objects.filter(uuid=request.POST.get("uuid", None)).first()
    if group and user not in group.group_members.all():
        group.group_members.add(user)
        group.save()
    return HttpResponseRedirect(reverse("home", kwargs={"uuid": "1"}))


@login_required(login_url="sign")
def home(request, uuid=None):
    user_group_factors = []
    user_groups = request.user.group_members.all()
    users = []
    this_group = None
    if user_groups:
        if uuid == "1":
            uuid = user_groups.first().uuid
        this_group = Group.objects.get(uuid=uuid)
        user_group_factors = Factor.objects.filter(factor_owner=request.user, factor_group__uuid=uuid)
        users = this_group.group_members.all()
    main_user = request.user

    talab = Factor.objects.filter(
        factor_owner=main_user, factor_group=this_group
    ).aggregate(
        price__sum=Coalesce(Sum('price'), 0)
    ).get("price__sum", 0)

    bedehi = Factor.objects.filter(
        factor_members=main_user, factor_group=this_group
    ).annotate(
        divided=Count('factor_members') + 1,
        sum_prices=Sum('price')
    ).aggregate(
        price_sum=Coalesce(F("sum_prices") / F("divided"), 0)
    )['price_sum'] or 0

    setattr(main_user, "talab", talab - bedehi)

    other_user = []
    for user in users:
        if main_user.id != user.id:
            talab = Factor.objects.filter(factor_owner=user, factor_group=this_group).aggregate(
                price__sum=Coalesce(Sum('price'), 0)).get(
                "price__sum", 0)
            bedehi = Factor.objects.filter(factor_members=user, factor_group=this_group).annotate(
                devided=Count('factor_members') + 1).aggregate(price_sum=Coalesce(Sum('price') / F("devided"), 0))[
                "price_sum"]
            setattr(user, "talab", talab - bedehi)
            other_user.append(user)

    contex = {
        "groups": user_groups,
        "user_factors": user_group_factors,
        "users": other_user,
        "group": this_group,
        "main_user": main_user
    }
    return render(request, 'index.html', contex)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("sign"))


def serve_file(http_request, path):
    return sendfile(http_request, MEDIA_ROOT + "/" + path)


def add_factor(request):
    kala_list = json.loads(request.POST.get("factor"))
    uuid = request.POST['uuid']
    group = Group.objects.filter(uuid=uuid).first()
    for kala in kala_list:
        factor = Factor(name=kala['kala'], price=int(kala['cost']), factor_owner=request.user, factor_group=group)
        factor.save()
        factor.factor_members.set(kala['userId'])
        factor.factor_members.add(request.user)
        factor.save()
    return HttpResponseRedirect(reverse("home", kwargs={"uuid": uuid}))

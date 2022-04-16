from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Entry
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'app_app/register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("app_app:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app_app/login.html", context={"login_form": form})


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")


def urls(request):
    return render(request, 'app_app/urls.html')
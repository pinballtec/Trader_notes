from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("login")
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'app_app/register.html', context={"register_form": form})


def login_request(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('entry-list')
    return render(request, 'app_app/login.html', {'page': page})


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content", "price", "shares", "date_created"]
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


def logout_page(request):
    logout(request)
    return redirect('login')
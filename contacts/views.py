from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Contact
from .forms import ContactForm, CustomUserCreationForm, CustomAuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 5)  # Show 5 contacts per page.
    page_number = request.GET.get('page', 1)
    page_contacts = paginator.get_page(page_number)
    return render(request, 'contacts/index.html', {'contacts': page_contacts})
    # return render(request, 'contacts/index.html', {
    #     'contacts': Contact.objects.all(),
    # })

def viewContact(request, id):
    contact = Contact.objects.get(pk=id)
    return HTTPResponseRedirect(reverse('index'))


@login_required
def add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_phone_number = form.cleaned_data['phone_number']
            new_address = form.cleaned_data['address']
            new_comments = form.cleaned_data['comments']

            new_contact = Contact(
                user=request.user,
                first_name=new_first_name, 
                last_name=new_last_name, 
                phone_number=new_phone_number, 
                address=new_address, 
                comments=new_comments)
            new_contact.save()
            return render(request, 'contacts/add.html', {
                'form': ContactForm(),
                'success': True,
            })
    else:
        form = ContactForm()
    return render(request, 'contacts/add.html', {
        'form': form,
    })

@login_required
def edit(request, id):
    contact = Contact.objects.get(pk=id)
    if request.user != contact.user:
        return HttpResponseForbidden("You are not allowed to edit this contact.")
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return render(request, 'contacts/edit.html', {
                'form': form,
                'success': True,
            })
    else:
        contact = Contact.objects.get(pk=id)
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit.html', {
        'form': form,
    })

@login_required
def delete(request, id):
    contact = Contact.objects.get(pk=id)
    if request.user != contact.user:
        return HttpResponseForbidden("You are not allowed to edit this contact.")
    if request.method == 'POST':
        contact.delete()
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'contacts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'contacts/register.html', {'form': form})
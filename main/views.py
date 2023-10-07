from django.shortcuts import render, redirect
from .models import *
from . import forms


def home(request):
    return render(request, 'main/home.html')


def services(request):
    services_list = ServiceModel.objects.all()

    return render(request, 'main/services.html', {'services': services_list})


def lawyers(request):
    lawyers_list = LawyerModel.objects.all()
    return render(request, 'main/lawyers.html', {'lawyers': lawyers_list})


def tv(request):
    tv_list = TVModel.objects.all()

    return render(request, 'main/tv-shows.html', {'tv_shows': tv_list})


def certificates(request):
    certificates_list = CertificateModel.objects.all()

    return render(request, 'main/certificates.html', {'certificates': certificates_list})


def contact(request):
    form = forms.ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/contact.html', {'contact_form': form})


def memo(request):
    return render(request, 'main/memo.html')


def lawyer_detail(request, id):
    lawyer = LawyerModel.objects.get(id=id)
    return render(request, 'main/lawyer-detail.html', {'lawyer': lawyer})

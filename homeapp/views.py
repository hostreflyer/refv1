from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "home.html"

class CheckPageView(TemplateView):
    template_name = "check.html"

class FAQPageView(TemplateView):
    template_name = "faq.html"

class SuccessPageView(TemplateView):
    template_name = "success.html"

from .forms import CheckForm
def checkpageview(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            check = form.save()
            return redirect('success')
    else:
        form = CheckForm()
    return render(request, 'check.html', {'form': form})


def test(request):    
    return render(request, 'test.html')
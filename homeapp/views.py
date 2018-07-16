from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "home.html"

class CheckPageView(TemplateView):
    template_name = "check.html"

class FAQPageView(TemplateView):
    template_name = "faq.html"

# class TestPageView(TemplateView):
#     template_name = "test.html"


from .forms import CheckForm
def test(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = CheckForm()
    return render(request, 'test.html', {'form': form})

from .forms import PersonForm
def test2(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PersonForm()
    return render(request, 'test2.html', {'form': form})
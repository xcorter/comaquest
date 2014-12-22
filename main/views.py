from django.shortcuts import render
from django.views import generic
from main.models import About, Slider


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context['slider'] = Slider.objects.all()
        return context
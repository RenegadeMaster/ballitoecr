from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from locator.forms import VolunteerForm
from locator.models import *
from datetime import datetime, timedelta


class MainView(TemplateView):

    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patrollers'] = Patroller.objects.all()
        context['shifts'] = Shift.objects.all()
        context['watchpoints'] = WatchPoint.objects.all()
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        context['teams'] = Team.objects.filter(day__gte=today, day__lte=tomorrow).all()
        return context


class RegisterView(TemplateView):

    template_name = "volunteer.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VolunteerForm()
        return context
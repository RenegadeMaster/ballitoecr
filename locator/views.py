import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from locator.forms import VolunteerForm
from locator.models import *
from datetime import datetime, timedelta


def regenerate_teams():
    today = datetime.today()
    # we need some organisation of patrollers to start off
    tomorrow = today + timedelta(days=1)

    Team.objects.filter(day__lt=today).delete()

    all_shifts = Shift.objects.all()
    watchpoints = WatchPoint.objects.all()

    if Team.objects.count() == 0: # regenerate for today
        for w in watchpoints:
            for sh in all_shifts:
                team = Team()
                team.day = datetime.today().date()
                team.shift = sh
                team.watch_point = w
                team.save()
    return

class MainView(TemplateView):

    template_name = "main.html"

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     # Add products and stuff here
    #
    #     return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_patrollers = Patroller.objects.all()
        context['patrollers'] = all_patrollers
        all_shifts = Shift.objects.all()
        context['shifts'] = all_shifts
        watchpoints = WatchPoint.objects.all()
        context['watchpoints'] = watchpoints
        today = datetime.today()
        # we need some organisation of patrollers to start off
        tomorrow = today + timedelta(days=1)
        # Team.objects.all().delete()
        regenerate_teams()

        current_teams = Team.objects.filter(day__gte=today).all()
        in_teams = []
        point_teams = {}
        for team in current_teams:
            for p in team.patrollers.all():
                in_teams.append(p.id)

        not_in_teams = Patroller.objects.exclude(id__in=in_teams).all()

        for w in watchpoints:
            for sh in all_shifts:
                team = Team.objects.filter(shift=sh, watch_point=w).first()
                for p in not_in_teams:
                    if p.preferred_shifts.exists() and p.preferred_shifts.first()==sh and p.preferred_watchpoint.first()==w:
                        team.patrollers.add(p)
                        team.save()
                # team.patrollers = first_pass_patrollers

        all_teams = Team.objects.all()
        context['team_keys'] = []
        context['team_patrollers'] = {}
        for team in all_teams:
            if team.patrollers is not None and team.patrollers.count() > 0:
                key = 'sh_' + str(team.shift.id) + '_pt_'+str(team.watch_point.id)
                context['team_patrollers'][key] = [p for p in team.patrollers.all()]
                context['team_keys'].append(key)
        context['teams'] = all_teams
        # sh_{{ sh.id }}_pt-{{ point.id }}
        return context

def reassign_team(request):
    # post contains controller ID, source and destination id's
    body = request.body.decode()
    data = json.loads(body)
    print(data)
    # remove from Team A (if exists) add to team B
    patroller = Patroller.objects.get(pk=int(data['patroller_id']))
    try:
        old_team = Team.objects.filter(shift__id=int(data['source_shift']), watch_point__id=int(data['source_point'])).first()
        old_team.patrollers.remove(patroller)
        old_team.save()
    except:
        pass

    try:
        new_team = Team.objects.filter(shift__id=int(data['dest_shift']), watch_point__id=int(data['dest_point'])).first()
        if not patroller in new_team.patrollers.all():
            new_team.patrollers.add(patroller)
            new_team.save()
    except:
        pass


    return JsonResponse({'success': True})

class RegisterView(TemplateView):

    template_name = "volunteer.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here
        f = VolunteerForm(request.POST)
        new_volunteer = f.save()
        context['success'] = True
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Add products and stuff here
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VolunteerForm()
        return context
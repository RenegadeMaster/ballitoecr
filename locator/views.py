from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


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
        context['latest_articles'] = Article.objects.all()[:5]
        return context
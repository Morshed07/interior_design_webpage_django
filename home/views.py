from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from home.models import Contact,StartUpImage,StoryImage,WorkLog



# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context.update(
            {
                'storyimages' : StartUpImage.objects.filter(show=True),
                'banners' : StartUpImage.objects.filter(show=True),
                'worklogs' : WorkLog.objects.all()
            }
        )
        return context
    
            

class WorkLogDetails(DetailView):
    model = WorkLog
    template_name = 'details_page.html'
    slug_url_kwarg = 'slug'


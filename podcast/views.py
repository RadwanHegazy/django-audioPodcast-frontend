from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.http import Http404
class Home (TemplateView) :
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        action = Action(
            url=MAIN_URL + "/stage/v1/get/"
        )

        action.get()
        data = action.json_data()
        
        return {
            'podcasts' : data
        }
class Podcast(TemplateView) :
    template_name = 'podcast_home.html'

    def get(self, request, podcast_id) :
        action = Action(
            url=MAIN_URL + f'/stage/v1/get/{podcast_id}/'
        ) 

        action.get()

        if action.is_valid:
            context = action.json_data()
            return render(request, self.template_name, context)
        raise Http404(request)


class CreatePodcast(TemplateView) :
    template_name = 'podcast_create.html'
    
    @login_required
    def get(self, request, **kwargs) : 
        return render(request, self.template_name)
    
    @login_required
    def post(self, request, **kwargs):
        action = Action(
            url=MAIN_URL + '/stage/v1/create/',
            data={**request.POST},
            headers=kwargs['headers']
        )

        action.post()

        if action.is_valid:
            response = action.json_data()
            return redirect('podcast', response['id'])

        print(action.json_data()) 
        return redirect('create_podcast')
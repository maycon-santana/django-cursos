from django.shortcuts import render
from django.views.generic import TemplateView
from apiyoutube.settings import YOUR_GOOGLE_CLIENT_ID

import json, time
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['YOUR_GOOGLE_CLIENT_ID'] = YOUR_GOOGLE_CLIENT_ID

        return context
    @csrf_exempt
    def google_login(request):
        time.sleep(3)
        token = request.body
        token = token.decode("utf-8").encode("windows-1252").decode("utf-8")
        token = json.loads(token)
        token = token['id_token']

        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), YOUR_GOOGLE_CLIENT_ID)
            userid = idinfo['sub']
            print(idinfo)

        except ValueError:
            # Invalid token
            pass

        return render(request, "index.html")    

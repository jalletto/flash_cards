import os
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bot.slack_client import SlackClient

@csrf_exempt
def response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    # action_template = MessegeParser.parse(body)
    # response = ActionDispatcher.dispatch(action_template)
    
    user = body['event']['user']
    
    if user != 'U01CD4QHR97':
        slack_client = SlackClient()
        slack_client.open_conversation(["U01C06563L2"])
        
        state = State.objects.last()

        
            

        state.save()
        slack_client.send_messgage(message)

    return HttpResponse('ok')
    
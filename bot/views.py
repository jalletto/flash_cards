import os
import json
from bot.message_parser import MessageParser
from bot.action_dispatcher import ActionDispatcher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bot.slack_client import SlackClient

@csrf_exempt
def response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    action_template = MessageParser.parse(body)
    response = ActionDispatcher.dispatch(action_template)
    
    if response['is_slack_message']:

        slack_client = SlackClient()
        slack_client.open_conversation(["U01C06563L2"])
        slack_client.send_messgage(response['message'])

        return HttpResponse('ok')
    
    return HttpResponse(response['message'])

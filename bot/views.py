import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bot.slack_client import SlackClient
from bot.message_parser import MessageParser
from bot.action_dispatcher import ActionDispatcher

@csrf_exempt
def get_slack_response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    action_template = MessageParser.parse(body)
    response = ActionDispatcher.dispatch(action_template)

    if response['send_slack_message']:
        slack_client = SlackClient()
        slack_client.send_messgage(response['message'], ["U01C06563L2"])

        return HttpResponse('ok')

    return HttpResponse(response['message'])

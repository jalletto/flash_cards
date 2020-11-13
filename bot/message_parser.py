from decks.models import State
from bot.action_list import ACTION_LIST

class MessageParser:

    @classmethod
    def parse(cls, request_body):

        if 'event' in request_body:
            text = request_body['event']['text']

        if 'challenge' in request_body:
            response = {
                'action' : ACTION_LIST['challenge'],
                'text'   : request_body['challenge']
            }
        elif request_body['event']['user'] == 'U01CD4QHR97':
            response = {
                'action': ACTION_LIST['bot_user'],
                'text'  : text
            }
        elif State.there_is_an_active_question():
            response = {
                'action' : ACTION_LIST['answer_question'],
                'text'   : text
            }
        elif not State.there_is_an_active_question():
            response = {
                'action' : ACTION_LIST['ask_a_question'],
                'text'   : text
            }

        return response

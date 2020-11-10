from decks.models import State

class MessageParser:
    
    @classmethod
    def parse(cls, request_body):

        text = request_body['event']['text'] if request_body['event']['text']
        
        if 'challenge' in request_body:
            response = { 
                'action' : ACTION_LIST['challenge'],
                'text'   : body['challenge']
            }
        elif request_body['event']['user'] == 'U01CD4QHR97':
            response = {
                'action': ACTION_LIST['bot_user'],
                'text'  : text
            }
        elif State.is_active_question:
            response = {
                'action' : ACTION_LIST['answer_question'],
                'text'   : text
            }
        elif not State.is_active_question
            response = {
                'action' : ACTION_LIST['ask_a_question'],
                'text'   : text
            }


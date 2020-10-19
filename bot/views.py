import os
import json
from random import choice as random_choice
from slack import WebClient
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from decks.models import Deck, State
from bot.slack_client import SlackClient

@csrf_exempt
def response(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    if 'challenge' in body:
        return HttpResponse(body['challenge'])  
    
    user = body['event']['user']
    
    if user != 'U01CD4QHR97':
        slack_client = SlackClient()
        slack_client.open_conversation(["U01C06563L2"])
        
        state = State.objects.last()

        if state.answered == True:
            deck  = Deck.objects.first()
            card  = random_choice(deck.cards.all())
            State.objects.create(card=card)
            message = f'Como se dice {card.front} en espanol?'
        else:
            answer = body['event']['text']
            state.answered = True
            card = state.card

            if card.back in answer:
                state.correct = True
                message = f'Si! {card.back} es correcto.'
            else:
                state.correct = False
                message = f'No. La respuesta correcta es {card.back}' 

        state.save()
        slack_client.send_messgage(message)
        
        
        # If there is an active state object for the user
            # get the card
            # if the front was asked then check to see if the back matches the text of the message
            # if it does update the state to correct and send a confirmation message
            # if it doesn't then update teh state to incorrect and send a message
            
        
        

    return HttpResponse('ok')

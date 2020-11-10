from decks.models import Deck, State
from random import choice as random_choice

class AskQuestion:

    @classmethod
    def execute(cls):
        deck  = Deck.objects.first()
        card  = random_choice(deck.cards.all())
        State.objects.create(card=card)
        
        return f'Como se dice {card.front} en espanol?'
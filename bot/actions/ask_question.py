from random import choice as random_choice
from decks.models import Deck, State

class AskQuestion:

    @classmethod
    def execute(cls):
        deck = Deck.objects.first()
        card = random_choice(deck.cards.all())
        State.objects.create(card=card)

        return {'message' : f'Como se dice {card.front} en espanol?', 'send_slack_message' : True}

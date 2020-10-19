from django.contrib import admin
from decks.models import Deck, Card, State


admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(State)

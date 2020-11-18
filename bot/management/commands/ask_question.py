from datetime import datetime, timezone
from django.core.management.base import BaseCommand, CommandError
from decks.models import State
from bot.actions.ask_question import AskQuestion
from bot.slack_client import SlackClient
from IPython import embed

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if self.should_ask_question():
            response = AskQuestion.execute()
            slack_client = SlackClient()
            slack_client.send_messgage(response['message'], ["U01C06563L2"])
    
    def time_since_last_question_was_answered(self):
        return (datetime.now(timezone.utc) - State.objects.last().updated_at).seconds

    def should_ask_question(self):
        if State.there_is_an_active_question(): 
            return False
        elif self.time_since_last_question_was_answered() < 18: 
            return False
        else:
            return True

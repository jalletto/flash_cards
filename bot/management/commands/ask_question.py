from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from decks.models import State
from bot.actions.ask_question import AskQuestion
from bot.slack_client import SlackClient

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    todays_date_and_time = datetime.now()

    def handle(self, *args, **options):
        if self.should_ask_question():
            response = AskQuestion.execute()
            slack_client = SlackClient()
            slack_client.send_messgage(response['message'], ["U01C06563L2"])
            self.stdout.write("A question was sent to slack")
        else:
            self.stdout.write("No question sent.")

    def is_week_day(self):
        # weeday returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
        return self.todays_date_and_time.weekday() not in [5, 6]

    def is_between_8_and_3(self):
        # time is in UTC
        return self.todays_date_and_time.hour > 14 and self.todays_date_and_time.hour < 21

    def time_since_last_question_was_answered(self):
        return (datetime.now(timezone.utc) - State.objects.last().updated_at).seconds

    def should_ask_question(self):
        if not self.is_week_day() or not self.is_between_8_and_3():
            # cant have cron on heroku so check time and weekday here.
            return False
        elif State.there_is_an_active_question():
            # don't ask if there is already a question waiting to be answered.
            return False
        elif self.time_since_last_question_was_answered() < 1800:
            # don't ask if question was just asked less than 30 seconds ago.
            return False
        else:
            return True

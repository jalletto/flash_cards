from django.test import SimpleTestCase
from bot.management.commands.ask_question import Command
from django.core.management import call_command
from datetime import datetime


class TestAskQuestion(SimpleTestCase):
    # datetime.datetime(year, month, day, hour, )
    def test_is_week_day_on_weekday(self):
        command = Command()
        command.todays_date_and_time = datetime(2020, 11, 9, 3)
        is_monday = command.is_week_day()
        self.assertEqual(is_monday, True)
    
    def test_is_week_day_on_sunday(self):
        command = Command()
        command.todays_date_and_time = datetime(2020, 11, 8, 3)
        is_sunday = command.is_week_day()
        self.assertEqual(is_sunday, False)
    
    def test_is_between_9_and_3_during_time(self):
        command = Command()
        command.todays_date_and_time = datetime(2020, 11, 8, 11)
        is_during_9_and_3 = command.is_between_9_and_3()
        self.assertEqual(is_during_9_and_3, True)

    def test_is_between_9_and_3_not_during_time(self):
        command = Command()
        command.todays_date_and_time = datetime(2020, 11, 8, 16)
        is_not_during_9_and_3 = command.is_between_9_and_3()
        self.assertEqual(is_not_during_9_and_3, False)

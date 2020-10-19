import os
import json
from slack import WebClient


class SlackClient:

    def __init__(self):
        self.auth_token = os.getenv('BOT_USER_AUTH_TOKEN')
        self.web_client = WebClient(token=self.auth_token)

    def open_conversation(self,users):
        self.response = self.web_client.conversations_open(users=users)

    def send_messgage(self,message):
        response = self.web_client.chat_postMessage(
            channel=self.response['channel']['id'],
            text=message
        )    
# TODO
# close = client.conversations_close(channel=channel)

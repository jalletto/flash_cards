class BotUserResponse:

    @classmethod
    def execute(cls, _text):
        # right now we do nothing if the message is from the bot user so we return false
        # which should prevent a new message from being sent.
        return {'message' : 'ok', 'send_slack_message' : False}

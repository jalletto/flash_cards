class BotUser:

    @classmethod
    def execute(cls, test):
        # right now we do nothing if the message is from the bot user so we return false
        # which should prevent a new message from being sent.
        return {'message' : None, 'is_slack_message' : False } 
class ChallengeResponse:

    @classmethod
    def execute(cls, text):
        # text will be the challenge string sent from slack
        return {'message' : text, 'send_slack_message' : False}

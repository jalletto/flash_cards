from django.http import HttpResponse

class ChallengeResponse:

    @classmethod
    def execute(cls, text):
        # text will be the challenge string sent from slack
        return { 'message' : HttpResponse(text), 'is_slack_message' : False }  
        
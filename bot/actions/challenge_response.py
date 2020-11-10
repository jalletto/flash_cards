class ChallengeResponse:

    @classmethod
    def execute(cls, text):
        # text will be the challenge string sent from slack
        return HttpResponse(text)  
        
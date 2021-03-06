from decks.models import State

class CheckQuestionAnswer:

    @classmethod
    def execute(cls, answer):
        state = State.objects.last()
        state.answered = True
        card = state.card

        if card.back.lower() in answer.lower():
            state.correct = True
            message = f'Si! {card.back} es correcto.'
        else:
            state.correct = False
            message = f'No. La respuesta correcta es {card.back}'

        state.save()
        return {'message' : message, 'send_slack_message' : True}

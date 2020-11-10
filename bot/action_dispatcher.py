from bot.actions.ask_question import AskQuestion
from bot.actions.challenge_response import ChallengeResponse
from bot.actions.check_question_answer import CheckQuestionAnswer

class ActionDispatcher:

    @classmethod
    def dispatch(cls, action_template):
        action = action_template['action']
        text   = action_template['text']
        if action == ACTION_LIST['challenge']:
            return ChallengeResponse.execute(text)
        elif action == ACTION_LIST['bot_user']:
            return BotUserResponse.execute(text)
        elif action == ACTION_LIST['answer_question']:
            return CheckQuestionAnswer.execute(text)
        elif action == ACTION_LIST['ask_a_question']:
            return AskQuestion.execute()

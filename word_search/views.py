from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class WordPuzzle(Page):
    timeout_seconds = Constants.word_puzzle_seconds
    timer_text = 'Tempo per il completamento:'


class WordsFound(Page):
    form_model = models.Player
    form_fields = ['cows_found']

    def before_next_page(self):
        self.player.participant.vars['words_found'] = self.player.cows_found
        self.player.set_payoff()



page_sequence = [
    Introduction,
    WordPuzzle,
    WordsFound
]

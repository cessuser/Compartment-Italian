from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
4 Treatments: Low, High, Economy good, Economy bad
"""


class Constants(BaseConstants):
    name_in_url = 'Vignette'
    players_per_group = None
    num_rounds = 2

    dice_prize = 25




class Subsession(BaseSubsession):
    treatment = models.IntegerField(min=1, max=10)

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['trts'] = [random.choice([5,6,7,8])]
                p.participant.vars['trts'].append(random.choice([1,2,3,4]))
                random.shuffle(p.participant.vars['trts'])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice = models.IntegerField(label="Voer uw dobbelwaarde in:", widget=widgets.TextInput)
    real_die_value = models.IntegerField(min=1, max=6)
    cur_trt = models.IntegerField()
    treatment_label = models.StringField()


    q1 = models.IntegerField(label='Da elettore, come valuteresti il partito Alpha, il partito del Primo Ministro, se l"economia performa al di sotto delle aspettative? A sinistra si indica "molto male", e a destra "molto bene”.')
    q2 = models.IntegerField(label='Come elettore come valuteresti il partito Beta, il partito del ministro delle finanze, per un\'economia che ha prestazioni inferiori alle aspettative? A sinistra si indica "molto male" e a destra "molto bene"')
    q3 = models.IntegerField(label='Come elettore come valuteresti il Partito Gamma, il Partito del Ministro degli Affari Esteri, per un\'economia che va al di sotto delle aspettative? A sinistra si indica "molto male", e a destra "molto bene".')
    q4 = models.StringField(choices=['Partito Alpha', 'Partito Beta', 'Partito Gamma'], widget=widgets.RadioSelect,
                            label='4.Quale delle tre parti ritieni principalmente responsabile dei bassi tassi di crescita del PIL e dei livelli di disoccupazione più elevati?')
    a1 = models.StringField(choices=['Partito Alpha', 'Partito Beta', 'Partito Gamma'],
                            label='Tot welke partij behoort de Minister President? U verdient 100 ECUs voor het correcte antwoord.', widget=widgets.RadioSelect)
    a2 = models.StringField(choices=['Partito Alpha', 'Partito Beta', 'Partito Gamma'],
                            label='Tot welke partij behoort de Minister van Financiën? U verdient 100 ECUs voor het correcte antwoord. ', widget=widgets.RadioSelect)
    a3 = models.StringField(choices=['Partito Alpha', 'Partito Beta', 'Partito Gamma'],
                            label='Tot welke partij behoort de Minister van Buitenlandse Zaken? U verdient 100 ECUs voor het correcte antwoord.', widget=widgets.RadioSelect)

    def set_payoff(self):
        self.payoff = Constants.dice_prize * sum(self.participant.vars['dice1'])
        if self.a1 == 'Partito Alpha':
            self.payoff += 100
        if self.a2 == 'Partito Beta':
            self.payoff += 100
        if self.a3 == 'Partito Gamma':
            self.payoff += 100

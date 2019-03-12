from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random

class ActionTest(Action):
   def name(self):
      return "projeto_aleatorio"

   def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Estou procurando um dos projetos cadastrados no SALIC:")
        try:
          req = requests.request('GET', "http://api.salic.cultura.gov.br/v1/projetos/")
          quantity = req.json()['count']
          a = req.json()['_embedded']['projetos'][random.randint(0, quantity)]['nome']
          dispatcher.utter_message(a)
        except ValueError:
          dispatcher.utter_message("Não consegui me conectar com o SALIC :/")
          dispatcher.utter_message(ValueError)


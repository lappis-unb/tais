from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import logging

logger = logging.getLogger(__name__) 

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
          logger.error(ValueError)

class ActionInformacaoProjeto(Action):
  def name(self):
    return "informacao_projeto"
  
  def run(self, dispatcher, tracker, domain):
    pronac = tracker.current_slot_values()['pronac']
    try:
      req = requests.request('GET', "http://api.salic.cultura.gov.br/v1/projetos/{}".format(pronac))
      logger.warning('===================================')
      logger.warning(req.json()['nome'])
      logger.warning(req.json()['ano'])
      logger.warning(req.json()['etapa'])
      logger.warning('===================================')
      dispatcher.utter_message("seu pronac é {}".format(pronac))
    except ValueError:
      dispatcher.utter_message("Não consegui me conectar com o SALIC :/")
      logger.error(ValueError)


from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import random
import logging
import datetime

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

      project_name = req.json()['nome']
      project_abstract = req.json()['resumo']
      proponente = req.json()['proponente']
      date = req.json()['data_inicio'].split('-')
      project_start_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))

      message = "Projeto {}\nEnviado por {} em {}\n{}\n".format(project_name.lower().title(),
                                                              proponente.lower().title(),
                                                              project_start_date.strftime("%d/%m/%Y"),
                                                              project_abstract)
      logger.warning(message)
      dispatcher.utter_message(message)

    except ValueError:
      dispatcher.utter_message("Não consegui me conectar com o SALIC :/")
      logger.error(ValueError)


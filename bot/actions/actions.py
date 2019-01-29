from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
        try:
          dispatcher.utter_message("Essa é uma custom action de test!")
          req = requests.request('GET', "http://api.salic.cultura.gov.br/v1/projetos/")
          dispatcher.utter_message(str(req.status_code))
        except ValueError:
          dispatcher.utter_message(ValueError)
          dispatcher.utter_message("----------")
          dispatcher.utter_message("svkjdkjvdhkjfdh")


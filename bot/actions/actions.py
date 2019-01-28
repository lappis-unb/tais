from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionTest(Action):
   def name(self):
      return "action_test"

   def run(self, dispatcher, tracker, domain):
      dispatcher.utter_message("Essa é uma custom action de test!")
      dispatcher.utter_message("Nova mensagem de teste")

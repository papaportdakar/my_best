# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
# 
# 
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# class ActionPrevision(Action):

#     def name(self) -> Text:
#         return "action_prevision"


#     async def run(self, 
#         dispatcher:CollectingDispatcher, 
#         tracker: Tracker, 
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         my_url = "https://www.portdakar.sn/"
#         dispatcher.utter_message("Nous vous demandons de regarder la section mouvements des navires sur le site du Port. Veuillez patienter nous allons ouvrir le site pour vous")
#         webbrowser.open(my_url)
#         return []
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
import time
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


class ActionPrevision(Action):

    def name(self) -> Text:
        return "action_prevision"


    async def run(self, 
        dispatcher:CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        my_url = "https://www.portdakar.sn/fr/infos-pratiques/previsions-trafic"
        buttons = []
        buttons.append({'title': 'Menu' , 'payload': '/menu_principal'})
        dispatcher.utter_message(text= f"Nous vous demandons de consulter la liste des navires à quai en cliquant sur le lien suivant: {my_url}" , buttons=buttons)
        print(my_url)
        # webbrowser.open(my_url)
        return []
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
import requests


class ActionAbout(Action):

    def name(self) -> Text:
        return "action_about"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Python here....Are you ready??")
        dispatcher.utter_message(text="Hello Shivank Here...How can I help You")

        return []

class ActionAbout(Action):
    
    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The time is  "+datetime.now().strftime("%H:%M:%S"))

        return []


class ActionShowDay(Action):
    
    def name(self) -> Text:
        return "action_show_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        week_num=datetime.now().weekday()
        

        dispatcher.utter_message(text="Today is  "+(week_days[week_num]))

        return []
    




class SearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        entities = tracker.latest_message['entities']
        print(entities)

    

        for e in entities:
            if e['entity'] == 'food_variety':
                name = e['value']

            if name == "north indian":
                message = "Restaurant North shahi --> Chhole Bhature, Kadhai Paneer, Rajma Chawal,Kadhi Chawal"
            if name == "south indian":
                message = "South wala --> Idly, Dosa, Sambhar, Vada"
            if name == "chinese":
                message = "Restaurant Chinese mania --> Manchurian, Chowmein, Spring Rolls, Momos"
            if name == "italian":
                message = "Restaurant Italian taste --> Pizza, Pasta, Bread and Tomato Soup, Panini"

        dispatcher.utter_message(text=message)

        return []

class ActionCoronaStatus(Action):

    def name(self) -> Text:
        return "action_corona_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()
        entities = tracker.latest_message['entities']
        print("Last message now", entities)
        state=None

        for e in entities:
            if e['entity'] == 'state':
                state = e['value']
        message="Please enter correct state name!"

        if((state =="india") or (state=="corona")):
            state = "Total"

        for data in response["statewise"]:
           # print(data["statecode"])
           # print(state.title())
            if(data["state"].lower()==state.lower()):
                print(data)
                message = "Active: "+data["active"] +" Confirmed: "+ data["confirmed"] +" Recovered: "+ data["recovered"] +" Deaths: "+ data["deaths"] +" Lastupdatedtime: "+ data["lastupdatedtime"]
                break
            elif(data["statecode"].lower()==state.lower()):
                print(data)
                message = "Active: "+data["active"] +" Confirmed: "+ data["confirmed"] +" Recovered: "+ data["recovered"] +" Deaths: "+ data["deaths"] +" Lastupdatedtime: "+ data["lastupdatedtime"]
                break
                
   
            
        
        print(message)
        dispatcher.utter_message(message)

        return []
import os
import requests
import json


def request_all_sheets():
   url = os.environ.get("SMARTSHEET_MAIN_API", "")
   payload = ""
   headers = {
      "Authorization": os.environ.get("SMARTSHEET_AUTH_TOKEN_API", "")
   }
   response = requests.request("GET", url, data=payload, headers=headers)
   
   return json.loads(response.text)


def request_sheet_syngenta_direct(id_sheet):
   url = os.environ.get("SMARTSHEET_MAIN_API", "") + id_sheet
   payload = ""
   headers = {
      "Authorization": os.environ.get("SMARTSHEET_AUTH_TOKEN_API", "")
   }
   response = requests.request("GET", url, data=payload, headers=headers)
   
   return json.loads(response.text) 
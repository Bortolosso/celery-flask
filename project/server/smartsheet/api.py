import os
import requests
import json


def request_all_sheets():
   url = os.environ.get("SMARTSHEET_MAIN_API", "https://api.smartsheet.com/2.0/sheets")
   payload = ""
   headers = {
      "Authorization": os.environ.get("SMARTSHEET_AUTH_TOKEN_API", "Authorization Bearer QjhvDfbr66ag0FKz1dIi6WpZqv95bMwdMbHqk")
   }
   response = requests.request("GET", url, data=payload, headers=headers)
   
   return json.loads(response.text)


def request_sheet_syngenta_direct(id_sheet):
   print(id_sheet)
   url = os.environ.get("SMARTSHEET_MAIN_API", "https://api.smartsheet.com/2.0/sheets")
   payload = ""
   headers = {
      "Authorization": os.environ.get("SMARTSHEET_AUTH_TOKEN_API", "Authorization Bearer QjhvDfbr66ag0FKz1dIi6WpZqv95bMwdMbHqk")
   }
   response = requests.request("GET", url, data=payload, headers=headers)
   
   return json.loads(response.text) 
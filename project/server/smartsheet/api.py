import requests


def request_all_sheets():
   url = "https://api.smartsheet.com/2.0/sheets"
   payload = ""
   headers = {"Authorization": "Authorization Bearer QjhvDfbr66ag0FKz1dIi6WpZqv95bMwdMbHqk"}
   response = requests.request("GET", url, data=payload, headers=headers)
   return response.text
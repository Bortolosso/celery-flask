import os
import pyodbc


def connect_db():
   str_conn = ("Driver={0};" "Server={1};" "Database={2};" "UID={3};" "PWD={4};").format(
      os.environ.get("DB_DRIVER", "{ODBC Driver 17 for SQL Server}"),
      os.environ.get("DB_SERVER", ""),
      os.environ.get("DB_DATABASE", ""),
      os.environ.get("DB_USER_UID", ""),
      os.environ.get("DB_PASSWORD", "")
   )
   
   print(str_conn)
   conn = pyodbc.connect(str_conn)
   
   return conn
import os
import pyodbc
import pymssql


def connect_db_pyodbc():
   str_conn = ("Driver={0};" "Server={1};" "Database={2};" "UID={3};" "PWD={4};").format(
      os.environ.get("DB_DRIVER", "{ODBC Driver 17 for SQL Server}"),
      os.environ.get("DB_SERVER", ""),
      os.environ.get("DB_DATABASE", ""),
      os.environ.get("DB_USER_UID", ""),
      os.environ.get("DB_PASSWORD", "")
   )
   
   conn = pyodbc.connect(str_conn)
   
   return conn


def connect_db_pymssql():
   # conn = pymssql.connect(
   #    server = str(os.environ.get("DB_SERVER", "")),
   #    user = str(os.environ.get("DB_USER_UID", "")),
   #    password = str(os.environ.get("DB_PASSWORD", "")),
   #    database = str(os.environ.get("DB_DATABASE", ""))
   # )
   
   conn = pymssql.connect(
      server = "BRAZIWADBP006.syngentaazure.org",
      user = "python_user",
      password = "Syngenta2020Syngenta2020",
      database = "DB_Grower"
   )  
   
   return conn
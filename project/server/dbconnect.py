import pyodbc


def connect_db():
   conn = pyodbc.connect(
      "Driver={ODBC Driver 17 for SQL Server};"
      "Server=BRAZIWADBP006.syngentaazure.org;"
      "Database=DB_Grower;"
      "UID=python_user;"
      "PWD=Syngenta2020Syngenta2020;"
   )
   cursor = conn.cursor()
   
   return cursor
import pyodbc
import pandas as pd1
from simple_salesforce import Salesforce
from datetime import datetime

from project.server.dbconnect import connect_db_pymssql


SALESFORCE_SELECT_QUERY = """
SELECT Id, Name, MobilePhone 
   FROM Contact LIMIT 100
"""

INSERT_DATA_TO_DBGROWER = """
INSERT INTO Teste (Id, Name, MobilePhone, DtCarga) 
   VALUES(?,?,?,?)
"""

def request_data_salesforce():
   salesfocer_connect = Salesforce(
      username='sytadmin@syngenta.com', 
      password='Syngenta1', 
      security_token=''
   )

   salesforce_data = salesfocer_connect.query_all(SALESFORCE_SELECT_QUERY)

   dataframe = pd1.DataFrame(salesforce_data['records']).drop(columns='attributes')
   print("Extração ETL bem sucedida")
   
   return dataframe


def init_get_sheet_syngenta_direct():
   conn = connect_db_pymssql()
   cursor = conn.cursor()

   cursor.execute("TRUNCATE TABLE Teste")
   conn.commit()
   
   dataframe_salesforce = request_data_salesforce()

   for index, row in dataframe_salesforce.iterrows():
      cursor.execute(
         INSERT_DATA_TO_DBGROWER, row.Id, row.Name, row.MobilePhone,datetime.now()
      )
      
   cursor.commit()
   cursor.close()
   
   return ("Dados incluidos com sucesso!")

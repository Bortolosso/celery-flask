import pyodbc
import pandas as pd1
from datetime import datetime, timezone

from simple_salesforce import Salesforce

from project.server.dbconnect import connect_db_pymssql

SALESFORCE_SELECT_QUERY = """
SELECT Id, Name, MobilePhone 
   FROM Contact 
   LIMIT 100
"""

INSERT_DATA_TO_DBGROWER = """
INSERT INTO [DB_Grower].[dbo].[Teste] 
(
   [Id], 
   [Name], 
   [MobilePhone], 
   [DtCarga]
) 
VALUES
   ('{0}', '{1}', '{2}', '{3}')
"""


def init_request_contact_sales_force():
   dataframe_salesforce = request_data_salesforce()
   
   return insert_into_db(dataframe_salesforce)


def request_data_salesforce():
   salesfocer_connect = Salesforce(
      username='sytadmin@syngenta.com', 
      password='Syngenta1', 
      security_token=''
   )

   salesforce_data = salesfocer_connect.query_all(SALESFORCE_SELECT_QUERY)
   
   dataframe = pd1.DataFrame(salesforce_data['records']).drop(columns='attributes')
   
   return dataframe.iterrows()


def insert_into_db(dataframe_salesforce):
   conn = connect_db_pymssql()
   cursor = conn.cursor()

   cursor.execute("TRUNCATE TABLE Teste")
   conn.commit()
   
   for index, row in dataframe_salesforce:
      try:
         date_now = datetime.now(timezone.utc)
         cursor.execute(INSERT_DATA_TO_DBGROWER.format(row.Id, row.Name, row.MobilePhone, str(date_now.strftime("%Y-%m-%d %H:%M:%S"))))
      except Exception as error:
            return str(error)
         
   conn.commit()
   conn.close()
   
   return "Data entered successfully."

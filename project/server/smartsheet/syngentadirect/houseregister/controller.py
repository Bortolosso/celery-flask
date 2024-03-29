import os

from datetime import datetime

from project.server.celery import celery
from project.server.smartsheet.api import request_sheet_syngenta_direct
from project.server.dbconnect import connect_db_pymssql

from project.server.scripts.smartsheet.convertjsontoinsertquery import convert



INSERT_SHEET_SYNGENTA_DIRECT = """
INSERT INTO [DB_Grower].[etl].[ts_smartsheet_syngentadirect]
(
    [nomerazaosocial],
    [cpfcnpj],
    [municipiouf],
    [regional],
    [rtvspoca],
    [emailrtv],
    [data],
    [ano],
    [nterritorio],
    [areasoja],
    [areamilho],
    [areafeijao],
    [areaoutrasculturas],
    [potencial],
    [statusentrada],
    [statusleadpotenciais],
    [aprovadorhistorico],
    [statushistorico],
    [aprovadorgtm],
    [statusgtm],
    [aprovadorcredito],
    [statuscredito],
    [aprovadorcomercial],
    [statuscomercial],
    [revisaogtm],
    [statuslead],
    [statusprocesso],
    [utimaatualizacao]
)
VALUES 
    ({0})
"""


def init_get_sheet_syngenta_direct_approved_leads():
    response_data = request_sheet_syngenta_direct(
        os.environ.get(
            "SHEET_ID_SYNGENTA_DIRECT_approved_LEADS",
            "gwwF5MG9Rh6xjr9XjpcMGp5xpc7fRhc3h6w9cFc1",
        )
    )
    print(convert(response_data['columns']))
    
   #  rows = response_data["rows"]

   #  conn = connect_db_pymssql()
   #  cursor = conn.cursor()

   #  # Clear content data table
   #  #  cursor.execute("TRUNCATE TABLE [DB_Grower].[etl].[TS_SMARTSHEET_SyngentaDirectapprovedLeads]")

   #  for i in rows:
   #      data_column = ""
   #      len_data = len(i["cells"]) - 1
   #      for index, data in enumerate(i["cells"]):
   #          value_ = data["displayValue"] if "displayValue" in data else ""
   #          data_column += (
   #              "'{0}'".format(value_.replace("'", " "))
   #              if index == len_data
   #              else "'{0}',".format(value_.replace("'", " "))
   #          )
   #      try:
   #          cursor.execute(INSERT_SHEET_SYNGENTA_DIRECT.format(data_column))
   #          success = True
   #      except Exception as error:
   #          return str(error)

   #  conn.commit()
   #  conn.close()

   #  return success

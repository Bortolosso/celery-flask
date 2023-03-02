import os

from datetime import datetime

from project.server.smartsheet.api import request_sheet_syngenta_direct
from project.server.dbconnect import connect_db_pyodbc

def init_get_sheet_syngenta_direct():
    
    id_sheet = os.environ.get("SHEET_ID_SYNGENTA_DIRECT", "")
    response_data = request_sheet_syngenta_direct(id_sheet)
    
    # conn = connect_db_pyodbc()
    # cursor = conn.cursor()
    
    # # Clear content data table
    # cursor.execute("TRUNCATE TABLE [DB_Grower].[dbo].[Teste]")
    # cursor.commit()
    
    # for i in response_data['data']:
    #     print(i['name'])
    #     cursor.execute("INSERT INTO [DB_Grower].[dbo].[Teste] (Id, Name, MobilePhone, DtCarga) VALUES(?, ?, ?, ?)", i['id'], i['name'], i['accessLevel'], datetime.now())
    # cursor.commit()
    # cursor.close()

    row = True
    return(row)

from project.server.smartsheet.api import request_all_sheets
from project.server.dbconnect import connect_db

QUERY_TEST = """
SELECT TOP (100) [ID_Carga]
      ,[DtCarga]
      ,[Processamento]
      ,[ID_Configuracao]
      ,[Etapa]
      ,[Descricao]
      ,[Tempo]
      ,[QtdeLinhas]
      ,[Usuario]
  FROM [DB_Grower].[dbo].[TL_CargaDados]
"""

def return_controller():
    data = payload()

    return data


def payload():
    response_data = request_all_sheets()
    
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute(QUERY_TEST)
    row = cursor.fetchall()

    cursor.close()
    # print(row)

    return "SUCCESS"

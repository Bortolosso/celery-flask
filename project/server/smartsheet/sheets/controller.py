from datetime import datetime

from project.server.smartsheet.api import request_all_sheets
from project.server.dbconnect import connect_db_pymssql, connect_db_pyodbc


QUERY_TEST = """
SELECT TOP (5) [ID_Carga]
      ,[Processamento]
      ,[ID_Configuracao]
      ,[Etapa]
      ,[Descricao]
      ,[QtdeLinhas]
      ,[Usuario]
  FROM [DB_Grower].[dbo].[TL_CargaDados]
"""

INSERT_SHEETS = """
INSERT [DB_Grower].[dbo].[Teste2] 
    (Name, AccessLevel, Link, DtCreated, DtModified, DtCarga) 
VALUES 
    ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
"""


def query_select_test():
    conn = connect_db_pyodbc()
    cursor = conn.cursor()
    cursor.execute(QUERY_TEST)
    row = cursor.fetchall()
    cursor.close()


def init_get_all_sheets():
    response_data = request_all_sheets()

    conn = connect_db_pymssql()
    cursor = conn.cursor()

    # Clear content data table
    cursor.execute("TRUNCATE TABLE [DB_Grower].[dbo].[Teste2]")
    for i in response_data["data"]:
        cursor.execute(
            INSERT_SHEETS.format(
                i["name"],
                i["accessLevel"],
                i["permalink"],
                i["createdAt"],
                i["modifiedAt"],
                datetime.now(),
            )
        )
    conn.commit()
    conn.close()

    row = True
    return row

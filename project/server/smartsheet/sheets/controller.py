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


def query_select_test():
    conn = connect_db_pyodbc()
    cursor = conn.cursor()
    cursor.execute(QUERY_TEST)
    row = cursor.fetchall()
    print(row)
    cursor.close()


def init_get_all_sheets():
    response_data = request_all_sheets()
    
    conn = connect_db_pymssql()
    cursor = conn.cursor()
    
    # Clear content data table
    cursor.execute("TRUNCATE TABLE [DB_Grower].[dbo].[Teste]")
    
    cursor.execute('SELECT [Id],[Name],[MobilePhone],[DtCarga] FROM [DB_Grower].[dbo].[Teste3]')  
    row = cursor.fetchall()  
    
    print(row)
        
    cursor.close()

    row = True
    return(row)

QUERY_CREATE_TABLE = """
CREATE TABLE [etl].[TS_SMARTSHEET_SyngentaDirect](
   [Id] [varchar](255) NULL,[Name] 
   [varchar](255) NULL,[MobilePhone] 
   [varchar](255) NULL,[DataCriacao] 
   [varchar](255) NULL,
   [Valor] [varchar](255) NULL,
   [DtCarga] [datetime] NULL
) ON [PRIMARY]
"""

def convert(array):
   init_query = "CREATE TABLE [etl].[TS_SMARTSHEET_SyngentaDirect]("
   columns = ""
   final_query = ") ON [PRIMARY]"
   for i in array:
      columns += "[{0}] [varchar](255) NULL, ".format(i['title'])
      
   return init_query + columns + final_query
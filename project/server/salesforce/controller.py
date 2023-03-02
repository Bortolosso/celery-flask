import pyodbc
import pandas as pd1
from simple_salesforce import Salesforce
from datetime import datetime

#CONEXAO
conexao = pyodbc.connect(
   "Driver={SQL Server};"            
   "Server=BRAZIWADBP006.syngentaazure.org;"            
   "Database=DB_Grower;"            
   "UID=python_user;"            
   "PWD=Syngenta2020Syngenta2020;"
)

#### SALESFORCE ####
sf = Salesforce(
   username='sytadmin@syngenta.com', 
   password='Syngenta1', 
   security_token=''
)

sf_data = sf.query_all("select Id, Name, MobilePhone from Contact limit 100")

sf_df = pd1.DataFrame(sf_data['records']).drop(columns='attributes')
print("Extração ETL bem sucedida")

cursor = conexao.cursor()
cursor.execute("TRUNCATE TABLE Teste")
cursor.commit()
print("Truncate da tabela bem sucedida")

#### INSERIR DADOS SALESFORCE X SQL SERVER ####
cursor = conexao.cursor()

for index, row in sf_df.iterrows():
     cursor.execute("INSERT INTO Teste (Id,Name,MobilePhone,DtCarga) values(?,?,?,?)", row.Id, row.Name, row.MobilePhone,datetime.now())
cursor.commit()
cursor.close()
print("Dados incluidos com sucesso!")



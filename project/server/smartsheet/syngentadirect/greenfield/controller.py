import os

from datetime import datetime, timezone

from project.server.celery import celery
from project.server.smartsheet.api import request_sheet_syngenta_direct
from project.server.dbconnect import connect_db_pymssql
from project.server.scripts.smartsheet.convertjsontoinsertquery import convert


INSERT_SHEET_SYNGENTA_DIRECT = """
INSERT INTO [DB_Grower].[etl].[TS_SMARTSHEET_SyngentaDirect_GreenField]
(
    [NomeRazaoSocial]
    ,[CpfCnpj]
    ,[NSAPId]
    ,[MunicipioUf]
    ,[Regional]
    ,[RTVSPOCA]
    ,[EmailRTV]
    ,[Data]
    ,[Ano]
    ,[NTerritorio]
    ,[AreaSoja]
    ,[AreaMilho]
    ,[AreaFeijao]
    ,[AreaOutrasCulturas]
    ,[Potencial]
    ,[DescricaoAdicionalCliente]
    ,[StatusEntrada]
    ,[StatusLeadPotenciais]
    ,[AprovadorHistorico]
    ,[StatusHistorico]
    ,[AprovadorGTM]
    ,[StatusGTM]
    ,[AprovadorCredito]
    ,[StatusCredito]
    ,[AprovadorComercial]
    ,[StatusComercial]
    ,[ReprovadoComercialRevisaoGTM]
    ,[StatusLead]
    ,[StatusProcesso]
    ,[UtimaAtualizacao]
    ,[DtCarga]
)
VALUES 
    ({0})
"""


def init_get_sheet_syngenta_direct_greenfield():
    response_data = request_sheet_syngenta_direct(
        os.environ.get(
            "SHEET_ID_SYNGENTA_DIRECT", "Xxq7333J29m4Rf9XVHXmWrWxWMrjjcF34w28q891"
        )
    )

    conn = connect_db_pymssql()
    cursor = conn.cursor()

    # Clear content data table
    cursor.execute("TRUNCATE TABLE [DB_Grower].[etl].[TS_SMARTSHEET_SyngentaDirect_GreenField]")
    conn.commit()

    for i in response_data["rows"]:
        data_column = ""
        len_data = len(i["cells"]) + 1
        for index, data in enumerate(i["cells"]):
            value_ = data["displayValue"] if "displayValue" in data else ""
            value_ = value_.replace("'", " ")

            dt_carga = datetime.now(timezone.utc)
            dt_carga = str(dt_carga.strftime("%Y-%m-%d %H:%M:%S"))
            data_column += "'{0}',".format(value_)

        data_column += "'{0}'".format(dt_carga)

        try:
            cursor.execute(INSERT_SHEET_SYNGENTA_DIRECT.format(data_column))
        except:
            pass
        
        success = True

    conn.commit()
    conn.close()
    return success

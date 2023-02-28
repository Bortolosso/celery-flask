from project.server.smartsheet.api import request_all_sheets
from project.server.dbconnect import connect_db


def return_controller():
    data = payload()

    return data


def payload():
    response_data = request_all_sheets()

    cursor = connect_db()
    cursor.execute(
        "SELECT TOP (10) [Id], [AccountId], [AssistantName] FROM [DB_Grower].[etl].[TS_FIELO_Contact]"
    )
    row = cursor.fetchone()

    while row:
        print(row)
        # row = cursor.fetchone()

    return "SUCCESS"

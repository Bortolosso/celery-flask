from project.server.smartsheet.api import request_all_sheets
from project.server.dbconnect import connect_db



def get_data():
    data = request_all_sheets()
    print(data)
    return ''


def payload():
    response_data = get_data()
    for i in response_data:
        print(':', i)

    cursor = connect_db()
    cursor.execute("SELECT TOP (10) [Id], [AccountId], [AssistantName] FROM [DB_Grower].[etl].[TS_FIELO_Contact]")
    row = cursor.fetchone() 
    
    print ('KAKAKAKAKAKAKAK') 
    
    while row:
        print (row) 
        # row = cursor.fetchone()
        
    return 'SUCCESS'
    
from datetime import datetime

from project.server.dbconnect import connect_db_pymssql


INSERT_ADD_TEST = """
INSERT [DB_Grower].[dbo].[Teste] 
    (Id, Name, MobilePhone, DtCarga) 
VALUES 
    ('{0}', '{1}', '{2}', '{3}')
"""


def add_interable_db():
    conn = connect_db_pymssql()
    cursor = conn.cursor()

    # Clear content data table
    cursor.execute("TRUNCATE TABLE [DB_Grower].[dbo].[Teste]")
    row = 1
    for i in range(1000):
        name = f"Teste JB: {row}"
        cursor.execute(
            INSERT_ADD_TEST.format(
               row, name, "(+55)DD00000-0000", ''
            )
        )
        row += 1
    conn.commit()
    conn.close()

    return True

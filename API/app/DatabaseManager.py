import Database.DatabaseConnection as dbc

def Init_Database():
    with dbc.DatabaseConnection("database.db") as conn:
        pass
import os.path
from parser import use
def execute(query,user):

    try:
        database = use.parse(query)

        # validate permission for user
        # validateuser(database,user)
        if os.path.exists(database):
            print("Database Selected: '{}'".format(database))
            return database
        print("Database does not exist '{}'".format(database))
        return None
    except Exception as e:
        print(e)
        return None


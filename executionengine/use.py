import os.path
from queryparser import use
from accessuser import authentication
from datastructure.constants import ROOT_DIRECTORY
def execute(query,user):
    try:
        database = use.parse(query)

        # validate permission for user
        if os.path.exists(ROOT_DIRECTORY+"/"+database):
            if not authentication.hasaccess(user, database):
                print("Does not have access to the database")
                return None
            print("Database Selected: '{}'".format(database))
            return ROOT_DIRECTORY+"/"+database
        print("Database does not exist '{}'".format(database))
        return None
    except Exception as e:
        print(e)
        return None


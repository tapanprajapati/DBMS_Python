import os.path
from datastructure.constants import ROOT_DIRECTORY
from parser import use
def execute(query,user):

    try:
        database = use.parse(query)

        # validate permission for user
        # validateuser(database,user)
        if os.path.exists(ROOT_DIRECTORY+"/"+database):
            print("Database Selected: '{}'".format(database))
            return ROOT_DIRECTORY+"/"+database
        print("Database does not exist '{}'".format(database))
        return None
    except Exception as e:
        print(e)
        return None


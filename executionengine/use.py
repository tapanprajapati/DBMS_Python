import os.path
from datastructure.constants import ROOT_DIRECTORY
from parser import use
import json

def validateuser(database,user):
    with open(ROOT_DIRECTORY+"/"+database+"/permission.json") as permission:
        permission_json = json.load(permission)

        if permission_json["owner"]!=user and user not in permission_json["users"]:
            raise Exception("Not Allowed To Access Database '{}'".format(database))

def execute(query,user):

    try:
        database = use.parse(query)

        if os.path.exists(ROOT_DIRECTORY+"/"+database):
            # validate permission for user
            validateuser(database,user)
            print("Database Selected: '{}'".format(database))
            return ROOT_DIRECTORY+"/"+database
        print("Database does not exist '{}'".format(database))
        return None
    except Exception as e:
        print(e)
        return None


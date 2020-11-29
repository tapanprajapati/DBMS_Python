import parser.drop as parsedrop
import queryvalidator.drop as validatedrop
from datastructure.table import Table
from transaction import helper
from datastructure import constants
import os


def execute(database, query, transaction=None):
    try:
        parsetree = parsedrop.parse(query)
        parsetree.database = database
        validatedrop.validate(parsetree)

        lock = helper.typeoflock(database, parsetree.table)
        if transaction == None:
            if lock == constants.EXCLUSIVE:
                raise Exception("Table {} is locked by a transaction".format(parsetree.table))
            table = Table(database, parsetree.table)
        else:
            if parsetree.table in transaction.accessed_tables.keys():
                table = transaction.accessed_tables[parsetree.table]
            else:
                if lock == None or lock == constants.SHARED:
                    table = Table(database, parsetree.table, parsetree.columns)
                    helper.locktable(database, parsetree.table, constants.SHARED)
                    transaction.accessed_tables[parsetree.table] = table
                else:
                    raise Exception("Table {} is locked by a transaction".format(parsetree.table))

        tablename = parsetree.table
        directory = database
        ext = ".json"
        file = directory + "/" + tablename
        if os.path.exists(file):
            os.remove(file)
        file = directory + "/" + tablename + ext
        if os.path.exists(file):
            os.remove(file)
            print(f"The {tablename} has been successfully dropped")

    except Exception as e:
        print(e)
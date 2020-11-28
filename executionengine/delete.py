import parser.delete as parsedelete
import queryvalidator.delete as validatedelete
from datastructure.table import Table
from transaction import helper
from datastructure import constants


def execute(database, query, transaction=None):
    try:
        parsetree = parsedelete.parse(query)
        parsetree.database = database
        validatedelete.validate(parsetree)

        lock = helper.typeoflock(database, parsetree.table)
        if transaction==None:
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
        records_before_deletion = len(table.iterator())
        if parsetree.condition is not None:
            column = list(parsetree.condition.keys())[0]
            value = parsetree.condition[column]
            table = table.delete(column, value, parsetree.conditiontype)
            table.columns = parsetree.columns
            records_after_deletion = len(table.iterator())
            total_records_deleted = records_before_deletion - records_after_deletion
            print(f"{total_records_deleted} records have been successfully deleted")
        else:
            table = table.deletetable()
            print(f"{parsetree.table} table has been successfully deleted")

        table.save()

    except Exception as e:
        print(e)
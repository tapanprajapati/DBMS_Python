from datastructure.constants import Operation
from executionengine import insert,select,delete
import transaction.helper as helper

class Transaction():
    def __init__(self,database):
        self.accessed_tables = {}
        self.database = database
    def execute(self,query,operation):
        # return
        if operation == Operation.SELECT:
            select.execute(self.database, query,self)
        elif operation == Operation.INSERT:
            insert.execute(self.database, query,self)
        elif operation == Operation.UPDATE:
            # execution for update command
            pass
        elif operation == Operation.DELETE:
            delete.execute(self.database, query,self)
            pass
        elif operation == Operation.DROP:
            print("Cannot delete resource during transaction")
            pass
        elif operation == Operation.CREATE:
            print("Cannot create resource during transaction")
            pass
        elif operation == Operation.USE:
            print("Cannot change database during transaction")
        elif operation == Operation.GRANT:
            print("Cannot change permissions during transaction")
        elif operation == Operation.REVOKE:
            print("Cannot change permissions during transaction")
        elif operation == Operation.EXIT:
            print("Please commit or rollback transaction")
        elif operation == Operation.STRT_TRNAS:
            print("A transaction is already active")
        elif operation == Operation.COMMIT:
            self.commit()
        elif operation == Operation.ROLLBACK:
            self.rollback()
        else:
            print("Invalid Query")

        print()

    def commit(self):
        for table in self.accessed_tables:
            self.accessed_tables[table].save()
        self.unlocktables()
        print("Transaction Commited")
        pass
    def rollback(self):
        self.unlocktables()
        print("Transaction Rolled back")

    def unlocktables(self):
        for table in self.accessed_tables.keys():
            helper.unlocktable(database=self.database, table= table)
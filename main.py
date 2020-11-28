from executionengine import select,use,infoqueries,insert
import parser.basequeryoperation as bqo
import getpass
from datastructure.constants import Operation
from transaction.transaction import Transaction

global user
global active_transaction

def startdatabasesystem():
    authenticate()

    handle_queries()


def authenticate():

    username = str(input("Username: "))

    # check username, if does not exists ask to sign up

    # if not userexists(username):
        # signup(username) # password has to be encrypted

    # otherwise read password
    # else:
    password = getpass.getpass("Password: ")

        # valid =  authenticateuser(username,password)
        # if not valid:
            # print('Invalid Password')
            # exit(0)
        # else:
            # user = username


def handle_queries():
    global active_transaction
    database = None
    while True:
        query = str(input(">> "))

        operation = bqo.findoperation(query)

        if database is None and operation is not Operation.USE:
            print("Database not selected\n")
            continue

        if active_transaction != None:
            active_transaction.execute(query,operation)

            if operation == Operation.COMMIT or operation == Operation.ROLLBACK:
                active_transaction = None
            continue

        if operation == Operation.SELECT:
            select.execute(database,query)
        elif operation == Operation.INSERT:
            insert.execute(database,query)
        elif operation == Operation.UPDATE:
            # execution for update command
            pass
        elif operation == Operation.DELETE:
            # execution for update command
            pass
        elif operation == Operation.DROP:
            # execution for update command
            pass
        elif operation == Operation.CREATE:
            # execution for update command
            pass
        elif operation == Operation.USE:
            database = use.execute(query,user)
        elif operation == Operation.GRANT:
            # execution for update command
            pass
        elif operation == Operation.REVOKE:
            # execution for update command
            pass
        elif operation == Operation.SHW_TBLS:
            infoqueries.showtables(database)
        elif operation == Operation.DESC:
            infoqueries.describe(database,query)
        elif operation == Operation.STRT_TRNAS:
            active_transaction = Transaction(database)
            print("Transaction Started")
        elif operation == Operation.COMMIT:
            print("No active Transaction")
        elif operation == Operation.ROLLBACK:
            print("No active Transaction")
        elif operation == Operation.EXIT:
            break
        else:
            print("Invalid Query")

        print()


if __name__ == '__main__':
    user = None
    active_transaction = None
    startdatabasesystem()

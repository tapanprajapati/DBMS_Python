from executionengine import select, use, infoqueries, insert, update, create, grant, revoke, delete, drop
import queryparser.basequeryoperation as bqo
import accessuser.authentication as authentication
import getpass
from datastructure.constants import Operation, ROOT_DIRECTORY
from transaction.transaction import Transaction

global user


def startdatabasesystem():
    authenticate()
    handle_queries()


def authenticate():
    global user
    username = str(input("Username: "))
    if not authentication.userexist(username):
        print("User does not exist. Create a new account...")
        password = getpass.getpass("Enter Password: ")
        re_password = getpass.getpass("Confirm Password: ")

        if password==re_password:
            authentication.signup(username, password)
            print("Signup Successful")
        else:
            print("Passwords Do Not Match!!! Try Again")
    else:
        password = getpass.getpass("Enter Password: ")
        valid = authentication.authenticateuser(username, password)
        if not valid:
            print('Invalid Password')
            exit(0)
        else:
            print("Welcome!")
            user = username


def handle_queries():
    global user
    database = None
    active_transaction = None
    while True:
        query = str(input(">> "))

        operation = bqo.findoperation(query)


        if operation == Operation.EXIT:
            break
        if "CREATE DATABASE" in query.upper():
            create.execute(database,query,user)
        elif operation == Operation.GRANT:
            grant.execute(query,user)
        elif operation == Operation.REVOKE:
            revoke.execute(query,user)

        if database is None and operation is not Operation.USE:
            print("Database not selected\n")
            continue

        if active_transaction != None:
            active_transaction.execute(query, operation)

            if operation == Operation.COMMIT or operation == Operation.ROLLBACK:
                active_transaction = None
            continue

        if operation == Operation.SELECT:
            select.execute(database, query)
        elif operation == Operation.INSERT:
            insert.execute(database, query)
        elif operation == Operation.UPDATE:
            update.execute(database, query)
        elif operation == Operation.DELETE:
            delete.execute(database, query)
        elif operation == Operation.DROP:
            drop.execute(database, query)
        elif operation == Operation.CREATE:
            create.execute(database,query,user)
        elif operation == Operation.USE:
            database = use.execute(query, user)
        elif operation == Operation.SHW_TBLS:
            infoqueries.showtables(database)
        elif operation == Operation.DESC:
            infoqueries.describe(database, query)
        elif operation == Operation.STRT_TRNAS:
            active_transaction = Transaction(database)
            print("Transaction Started")
        elif operation == Operation.COMMIT:
            print("No active Transaction")
        elif operation == Operation.ROLLBACK:
            print("No active Transaction")
        else:
            print("Invalid Query")

        print()


if __name__ == '__main__':
    user = None
    startdatabasesystem()

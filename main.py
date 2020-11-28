from executionengine import select,use,infoqueries,insert,update,create,grant,revoke
import queryparser.basequeryoperation as bqo
import accessuser.authentication as authentication
from datastructure.constants import Operation
from transaction.transaction import Transaction


global user
global active_transaction


def startdatabasesystem():
    authenticate()

    handle_queries()


def authenticate():
    username = str(input("Username: "))
    if not authentication.userexist(username):
        print("User does not exist. Create a new account...")
        password = str(input("Please input password: "))
        authentication.signup(username, password)
    else:
        password = str(input("Password: "))
        valid = authentication.authenticateuser(username, password)
        if not valid:
            print('Invalid Password')
            exit(0)
        else:
            print("Welcome!")
            user = username


def handle_queries():
    global active_transaction
    database = None
    while True:
        query = str(input(">> "))

        operation = bqo.findoperation(query)

        # if database is None and operation is not Operation.USE:
        #     print("Database not selected\n")
        #     continue

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
            update.execute(database,query)
        elif operation == Operation.DELETE:
            # execution for update command
            pass
        elif operation == Operation.DROP:
            # execution for update command
            pass
        elif operation == Operation.CREATE:
            create.execute(query)
            # if query.split()[1] == "DATABASE":
            #     database = query.split()[2]
            #     path = "dbms\\" + database + "\\permission.json"
            #     permission = {"owner": user, "user":[]}
            #     with open(path, "w", encoding="utf-8") as file:
            #         file.write(json.dumps(permission, indent=4, ensure_ascii=False))
        elif operation == Operation.USE:
            database = use.execute(query,user)
        elif operation == Operation.GRANT:
            grant.execute(query)
        elif operation == Operation.REVOKE:
            revoke.execute(query)
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


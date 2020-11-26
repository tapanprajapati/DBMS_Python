import executionengine.insert as insert
import executionengine.select as select
import executionengine.use as use
import parser.basequeryoperation as bqo
import getpass
from datastructure.constants import Operation

user = None

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
    database = None
    try:
        while True:
            query = str(input(">> "))

            operation = bqo.findoperation(query)

            if database is None and operation is not Operation.USE:
                print("Database not selected")

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
            elif operation == Operation.EXIT:
                break

            print()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    startdatabasesystem()

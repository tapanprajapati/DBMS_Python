from datastructure.constants import Operation

def findoperation(query):
    operation = query.split(" ")[0].upper()

    if operation == 'SELECT':
        return Operation.SELECT
    if operation == 'INSERT':
        return Operation.INSERT
    if operation == 'UPDATE':
        return Operation.UPDATE
    if operation == 'DELETE':
        return Operation.DELETE
    if operation == 'CREATE':
        return Operation.CREATE
    if operation == 'DROP':
        return Operation.DROP
    if operation == 'EXIT':
        return Operation.EXIT
    if operation == 'USE':
        return Operation.USE
    if operation == 'GRANT':
        return Operation.GRANT
    if operation == 'REVOKE':
        return Operation.REVOKE
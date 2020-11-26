import enum

# comparison operators
class Compare(enum.Enum):
    EQ = 0
    LT = 1
    GT = 2
    LE = 3
    GE = 4

class Metadata():
    COLUMNS = 'columns'
    COLUMNS_NAME = 'name'
    COLUMNS_TYPE = 'type'
    COLUMNS_LENGTH = 'length'

    KEYS = 'keys'
    KEYS_PRIMARY = 'primary'
    KEYS_FOREIGN = 'foreign'
    KEYS_FOREIGN_NAME = 'name'
    KEYS_FOREIGN_REF_TABLE = 'ref_table'
    KEYS_FOREIGN_REF_COLUMN = 'ref_column'

    VARCHAR = "VARCHAR"
    INT = "INT"
    DOUBLE = "DOUBLE"

ALLOWED_COMPARATORS = ['<','>','=','<=','>=']

class Operation(enum.Enum):
    SELECT = 'select'
    UPDATE = 'update'
    INSERT = 'insert'
    DELETE = 'delete'
    DROP = 'drop'
    CREATE = 'create'
    GRANT = 'grant'
    REVOKE = 'revoke'
    EXIT = 'exit'
    USE = 'use'
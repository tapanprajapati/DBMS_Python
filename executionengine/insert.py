from datastructure.supporting_structures import Record
import parser.insert as parseinsert
import queryvalidator.insert as validateinsert
from datastructure.table import Table

def execute(database,query):
    try:
        parsetree = parseinsert.parse(query)
        parsetree.database = database
        validateinsert.validate(parsetree)

        t = Table(database,parsetree.table)
        record = Record()
        record.data = parsetree.columnvaluepair

        t.save()
    except Exception as e:
        print(e)


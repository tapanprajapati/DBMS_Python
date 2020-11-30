from queryparser import update
import queryvalidator.update as validateupdate
from datastructure.table import Table


def execute(database, query):
    try:
        parsetree = update.parse(query)
        parsetree.database = database
        validateupdate.validate(parsetree)

        table = Table(database, parsetree.table)

        column = list(parsetree.condition.keys())[0]
        value = parsetree.condition[column]
        rows = table.update(parsetree.columnvaluepair, column, value, parsetree.conditiontype)

        print("{} Rows Updated".format(rows))
        table.save()
    except Exception as e:
        print(e)
import parser.select as parseselect
import queryvalidator.select as validateselect
from datastructure.table import Table
from prettytable import PrettyTable

def execute(database,query):
    try:
        parsetree = parseselect.parse(query)
        parsetree.database = database
        validateselect.validate(parsetree)

        table = Table(database,parsetree.table,parsetree.columns)

        if parsetree.condition is not None:
            column = list(parsetree.condition.keys())[0]
            value = parsetree.condition[column]
            table = table.filter(column,value,parsetree.conditiontype)
            table.columns = parsetree.columns

        if parsetree.columns is None:
            columns = table.metadata.columns
        else:
            columns = parsetree.columns
        ptable = PrettyTable(columns)

        for row in table.iterator():
            data = []
            for column in columns:
                data.append(row.data[column])
            ptable.add_row(data)
        print(ptable)
    except Exception as e:
        print(e)
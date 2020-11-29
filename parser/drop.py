from parser.parsetree import ParseTree
import re


def validate_query(query):
    pattern = re.compile('DROP\s+TABLE(.*?)\s+;')
    if pattern.match(query):
        return True
    else:
        return False


def extract_table_name(query):
    name = re.search('TABLE(.*);', query)
    print(f"the table name is : {name.group(1).strip()}")
    return name.group(1).strip()


def parse(drop_query):
    parsetree = ParseTree()
    drop_query = drop_query.upper()
    drop_query = re.sub(r"\s+", " ", drop_query)
    drop_query.strip()
    if not validate_query(drop_query):
        raise Exception("The Drop query is not valid")
    table_name = extract_table_name(drop_query)
    parsetree.table = table_name
    return parsetree
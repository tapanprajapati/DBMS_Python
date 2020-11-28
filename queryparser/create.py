import re
import json
import os


def __getdatabasename(query):
    databasename_re = re.search(r'DATABASE .*$', query).group()
    databasename = databasename_re.replace("DATABASE", "").strip()
    return databasename


def __gettablename(query):
    tablename_re = re.search(r'TABLE .*\(', query).group()
    tablename = tablename_re.replace("TABLE", "").strip()
    tablename = tablename[:tablename.find('(')].strip()
    return tablename


def __getcolumns(query):
    columns = re.findall(r'[(](.*)[)]', query)[0]
    columns = re.findall(r'(?:[^,(]|\([^)]*\))+', columns)
    columns = list(map(lambda x: x.strip(), columns))
    metadata = {"columns":[], "keys": {}}
    columnlist = []
    for e in columns:
        pair = list(map(lambda x: x.strip(), e.split()))
        if pair[0] == "PRIMARY":
            primarykey = re.findall(r'[(](.*)[)]', e)[0].split(",")
            primarykey = list(map(lambda x: x.strip(), primarykey))
            metadata["keys"] = {"primary":primarykey}
        column = {"name": pair[0]}
        if pair[1].find('(') > 0:
            datatype = pair[1][:pair[1].find('(')]
            column["type"] = datatype
            length = pair[1][pair[1].find('(') + 1:pair[1].find(')')]
            column["length"] = int(length)
        else:
            column["type"] = pair[1]
            if pair[1] == 'INT':
                column["length"] = 8
            elif pair[1] == 'DOUBLE':
                column["length"] = 16
            elif pair[1] == 'VARCHAR':
                column["length"] = 50
        columnlist.append(column)
        metadata["columns"] = columnlist
    return metadata


def parse(query):
    query = query.upper()
    parts = query.split()
    if parts[1] == "DATABASE":
        if len(parts) != 3:
            raise Exception("Invalid 'Create Database' query")
        # os.chdir(os.path.abspath(os.path.dirname(os.getcwd())))
        try:
            os.mkdir("dbms\\" + __getdatabasename(query))
            os.chdir("dbms\\" + __getdatabasename(query))
            file = open("permission.json", "w")
            file.close()
        except Exception as e:
            print(e)
    elif parts[1] == "TABLE":
        tablename = __gettablename(query)
        columnlist = __getcolumns(query)
        with open(tablename + "_meta.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(columnlist, indent=4, ensure_ascii=False))
        file = open(tablename + ".json", "w", encoding="utf-8")
        file.close()
    else:
        raise Exception("Invalid 'Create' query structure")






#parse("CREATE DATABASE GROUP9")
#parse("CREATE TABLE emp (id INT, name VARCHAR(45), PRIMARY KEY (id, name))")

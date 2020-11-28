from queryparser import create


def execute(query):
    try:
        create.parse(query)
    except Exception as e:
        print(e)
        return None



#execute("create database group")
#execute("create table emp (id int, name varchar(45))")

from queryparser import create


def execute(database,query,user):
    try:
        create.parse(database,query,user)
    except Exception as e:
        print(e)
        return None



#execute("create database group")
#execute("create table emp (id int, name varchar(45))")

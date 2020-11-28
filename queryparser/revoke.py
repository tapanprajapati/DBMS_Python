import json


def parse(query):
    # os.chdir(os.path.abspath(os.path.dirname(os.getcwd())))
    query = query.upper()
    database = query.split()[1]
    user = query.split()[2]
    path = "dbms\\" + database + "\\" + "permission.json"
    file = open(path, "r")
    permission = json.load(file)
    file.close()
    permission["user"].remove(user)
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(permission, indent=4, ensure_ascii=False))


#parse("REVOKE GROUP9 TAPAN")

import json


def signup(username, passward):
    # os.chdir(os.path.abspath(os.path.dirname(os.getcwd())))
    file = open("dbms\\user.json", "r")
    userlist = json.load(file)
    new_user = {"name":username, "passward":passward}
    userlist.append(new_user)
    with open("dbms\\user.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(userlist, indent=4, ensure_ascii=False))


def userexist(username):
    # os.chdir(os.path.abspath(os.path.dirname(os.getcwd())))
    file = open("dbms\\user.json", "r")
    userlist = json.load(file)
    file.close()
    for e in userlist:
        if e["name"] == username:
            return True
    return False


def authenticateuser(username, passward):
    # os.chdir(os.path.abspath(os.path.dirname(os.getcwd())))
    file = open("dbms\\user.json", "r")
    userlist = json.load(file)
    file.close()
    for e in userlist:
        if e["name"] == username and e["passward"] == passward:
            return True
    return False


import queryparser.grant as grant

def execute(query):
    try:
        grant.parse(query)
        return None
    except Exception as e:
        print(e)
        return None
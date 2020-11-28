import queryparser.revoke as revoke

def execute(query):
    try:
        revoke.parse(query)
        return None
    except Exception as e:
        print(e)
        return None
def parse(query):
    query = query.upper()

    parts = query.split(" ")

    if len(parts)!=2:
        raise Exception("Invalid 'Use' query structure")

    return parts[1]
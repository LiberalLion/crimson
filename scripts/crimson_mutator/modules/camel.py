def make_camel(payload):
    return "".join(
        payload[x].upper() if x % 2 == 0 else payload[x].lower()
        for x in range(len(payload))
    )

def make_upper(string):
    return string.upper()


def make_lower(string):
    return string.lower()



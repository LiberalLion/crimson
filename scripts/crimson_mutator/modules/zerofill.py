# from zerofill import make_zerofill
#Tamper payload, fill it with key words for WAF bypass 

def make_zerofill(string):
    return "".join(
        f"{string[x]}ZEROFILL" if string[x] != " " else string[x]
        for x in range(len(string))
    )



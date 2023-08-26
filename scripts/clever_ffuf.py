# THIS IS ADDON TO CRIMSON_TARGET
#
### CREATED BY KARMAZ
#
#
# FUNCTIONS:
#
# 1. Read the ffuf_status.txt
# 2. Count all responses
# 3. Count responses per status code
# 4. Check the rules.
#    
###
import re, os

# GET THE TARGET DOMAIN
target_domain = os.getenv("domain")

# ARRAYS WITH LINES OF STATUS CODE
status_all = []
status_200 = []
status_301 = []
status_302 = []
status_401 = []
status_403 = []
status_404 = []
status_429 = []
status_odd = []
final_list = []

with open("status_ffuf.txt", "r") as my_file:
    for line in my_file:
        status_all.append(line.rstrip().split("\"")[3])
        if "\"status\":200" in line:
            status_200.append(line.rstrip().split("\"")[3])
        elif "\"status\":301" in line:
            status_301.append(line.rstrip().split("\"")[3])
        elif "\"status\":302" in line:
            status_302.append(line.rstrip().split("\"")[3])
        elif "\"status\":401" in line:
            status_401.append(line.rstrip().split("\"")[3])
        elif "\"status\":403" in line:
            status_403.append(line.rstrip().split("\"")[3])
        elif "\"status\":404" in line:
            status_404.append(line.rstrip().split("\"")[3])
        elif "\"status\":429" in line:
            status_429.append(line.rstrip().split("\"")[3])
        else:
            status_odd.append(line.rstrip().split("\"")[3])

### COUNTERS
status_all_c = len(status_all)
status_200_c = len(status_200)
status_301_c = len(status_301)
status_302_c = len(status_302)
status_401_c = len(status_401)
status_403_c = len(status_403)
status_404_c = len(status_404)
status_429_c = len(status_429)
status_odd_c = len(status_odd)

### PRINT RESULTS
print(" DIR BRUTE STATUS ")
print(" ---------------- ")
print(f" TOTAL   : {status_all_c}")
print(
    f" 200     : {status_200_c} ({str(round(status_200_c / status_all_c, 3))}%)"
)
print(
    f" 301     : {status_301_c} ({str(round(status_301_c / status_all_c, 3))}%)"
)
print(
    f" 302     : {status_302_c} ({str(round(status_302_c / status_all_c, 3))}%)"
)
print(
    f" 401     : {status_401_c} ({str(round(status_401_c / status_all_c, 3))}%)"
)
print(
    f" 403     : {status_403_c} ({str(round(status_403_c / status_all_c, 3))}%)"
)
print(
    f" 404     : {status_404_c} ({str(round(status_404_c / status_all_c, 3))}%)"
)
print(
    f" 429     : {status_429_c} ({str(round(status_429_c / status_all_c, 3))}%)"
)
print(
    f" OTHER   : {status_odd_c} ({str(round(status_odd_c / status_all_c, 3))}%)"
)
print(" ---------------- ")

### MAIN FUNCTIONALITY
# Do not store:
#   429 - too many requests
print("\n AFTER CHANGE RESULTS ")
print(" ---------------- ")
if (status_200_c / status_all_c) < 0.3:   
    final_list.extend(status_200)
    print(
        f" 200     : {status_200_c} ({str(round(status_200_c / status_all_c, 3))}%)"
    )
elif (status_301_c / status_all_c) < 0.001:
    final_list.extend(status_301)
    print(
        f" 301     : {status_301_c} ({str(round(status_301_c / status_all_c, 3))}%)"
    )
elif (status_302_c / status_all_c) < 0.001:
    final_list.extend(status_302)
    print(
        f" 302     : {status_302_c} ({str(round(status_302_c / status_all_c, 3))}%)"
    )
elif (status_401_c / status_all_c) < 0.001:
    final_list.extend(status_401)
    print(
        f" 401     : {status_401_c} ({str(round(status_401_c / status_all_c, 3))}%)"
    )
elif (status_403_c / status_all_c) < 0.001:
    final_list.extend(status_403)
    print(
        f" 403     : {status_403_c} ({str(round(status_403_c / status_all_c, 3))}%)"
    )
elif (status_404_c / status_all_c) < 0.001:
    final_list.extend(status_404)
    print(
        f" 404     : {status_404_c} ({str(round(status_404_c / status_all_c, 3))}%)"
    )
else:
    final_list.extend(status_odd)
    print(
        f" OTHER   : {status_odd_c} ({str(round(status_odd_c / status_all_c, 3))}%)"
    )

print(f" TOTAL   : {len(final_list)}")
print(" ---------------- ")


with open("temp_ffuf.txt","w") as output_file:
    for line in final_list:
        output_file.write(line + "\n")

'''
import re
from collections import Counter

c = Counter()
with open("status_ffuf.txt", "r") as my_file:
    sep = ' '
    without_first = [sep.join(line.split(sep)[1:]).strip() for line in my_file.readlines()]
    c = Counter(without_first)
    result = {}
    for key, count in c.items():
        print(key.strip(), count)
        result[re.search(r"Status: (\d{3})", key).group(1)] = count
    print(result)
for line in final_list:'''

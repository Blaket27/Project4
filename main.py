import pathlib
import re
import urllib.request
import zipfile
from datetime import datetime
from collections import Counter

# file = pathlib.Path("./http_access_log.txt")
# url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# urllib.request.urlretrieve(url, "./http_access_log.txt")

ERRORS = []
# These are counter variables
days = {
    0: 1,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
weeks = {
}
months = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
}
failed_request = 0
redirect_request = 0
total_count = 0
file_count = {}

# Dictionary to store log lines by month
lines_by_month = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}


entire_log = [
    'local - - [24/Jan/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 300 150',
    'local - - [24/Jan/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 300 150',
    'local - - [24/Jan/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 400 1210',
    'local - - [24/Jan/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 400 1210',
    'local - - [24/Jan/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 400 1210',
    'local - - [24/Dec/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185'
 ]


regex = re.compile('(.*?) - - \[(.*?):(.*) .*\] \"[A-Z]{3,6} (.*?) HTTP.*\" (\d{3}) (.+)')

for line in entire_log:
    total_count += 1

    parts = regex.split(line)

    if len(parts) != 8:
        continue

    timestamp = datetime.strptime(parts[2], '%d/%b/%Y')
    filename = parts[4]
    months[timestamp.month] += 1
    days[timestamp.weekday()] += 1

    week_num = timestamp.isocalendar()[1]
    if week_num in weeks:
        weeks[week_num] += 1
    else:
        weeks[week_num] = 1

    if filename in file_count:
        file_count[filename] += 1
    else:
        file_count[filename] = 1

    if parts[5][0] == "4":
        failed_request += 1

    if parts[5][0] == "3":
        redirect_request += 1

    lines_by_month[timestamp.month].append(line)

# for key, value in lines_by_month:
    # Open new file for this month
    # Write Loglines into file
    # fh = open(f"{key}.txt", 'w')
    # for line in value:
      #   fh.write(line)
   #  fh.close()

    #print(timestamp.month)
    # if timestamp.month not in weeks:
        # weeks.append(timestamp.month)
    # weeks[timestamp.weekday()] += 1

#print(months)
#print("The total number of requests made is " + str(total_count))


print(f"The total number of requests made is {total_count}.")
for key, value in days.items():
    print(f"{key} has {value} logged access attempts.")
for key, value in months.items():
    print(f"{key} had {value} logged access attempts.")
print("The number of failed requests is " + str((failed_request/total_count)*100) + "%.")
print("The number of redirected requests is " + str((redirect_request/total_count)*100) + "%.")
most_requested = value, count = Counter(file_count.values()).most_common(1)[0]
print(f"The most requested file was " + str(most_requested))

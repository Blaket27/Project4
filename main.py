import pathlib
import re
import urllib.request
from datetime import datetime

ERRORS = []
days = {}
weeks = {}
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
total_count = 0


# file = pathlib.Path("./http_access_log.txt")
entire_log = [
    'local - - [24/Jan/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150',
    'local - - [24/Jan/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 200 1210',
    'local - - [24/Dec/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185'
 ]


# url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# urllib.request.urlretrieve(url, "./http_access_log.txt")
regex = re.compile('(.*?) - - \[(.*?):(.*) .*\] \"[A-Z]{3,6} (.*?) HTTP.*\" (\d{3}) (.+)')

for line in entire_log:
    total_count += 1

    parts = regex.split(line)
    timestamp = datetime.strptime(parts[2], '%d/%b/%Y')
    if len(parts) != 8:
        continue

    months[timestamp.month] += 1

    print(timestamp.month)
    # if timestamp.month not in weeks:
        # weeks.append(timestamp.month)
    # weeks[timestamp.weekday()] += 1

print(months)
print("The total number of requests made is " + str(total_count))

for key, value in months.items():
    print(key, ' had ', value, ' logged access attempts.')

for key, value in weeks.items():


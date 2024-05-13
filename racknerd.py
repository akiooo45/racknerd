#!/usr/bin/env python

import requests
# import re
key =
hash =
action = 'info'

url = f'https://nerdvm.racknerd.com/api/client/command.php?key={key}&hash={hash}&action={action}&bw=true'

response = requests.get(url)
# print(response.text)

bw_info = response.text

#print(bw_info.split(','))

bw = bw_info.split(',')[2]
free_bw = float(bw) / (1024 ** 3)
free_bw = round(free_bw,1)
print("流量还有:",free_bw, "GB")


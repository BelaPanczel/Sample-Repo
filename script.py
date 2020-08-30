import math
import os
import sys

import requests


# print(greet('World'))
# print(greet('BC'))

r = requests.get("https://www.google.com/")
print(r.status_code)
print(r.ok)
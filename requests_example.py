#!/usr/bin/env python3
import requests

response = requests.get("http://httpbin.org/get")
print(response.status_code)
print(response.text)

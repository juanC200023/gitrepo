#!/usr/bin/env python3
import requests


values = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

response = requests.get("https://httpbin.org/get", params=values)
#response = requests.post("https://httpbin.org/post", data=payload)
print(f"\n[+] URL final: {response.url}")
print(response.text)

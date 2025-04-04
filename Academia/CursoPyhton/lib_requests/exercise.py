#!/usr/bin/env python3

import requests

response = requests.get("https://google.es")

print(f"\n[+] Status code: {response.status_code}")
print(f"\n[+] Mostrando codigo fuente de la respuesta:\n")

with open("index.html", "w") as f:
    f.write(response.text)

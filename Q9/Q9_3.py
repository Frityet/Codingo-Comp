# Write your code here!

import requests
open("msg.txt", "w").write(requests.get("http://8c88-2001-569-52a4-5200-cb3-8e5e-382b-2f12.ngrok.io/get").json()["message"])

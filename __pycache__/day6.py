import urllib.request as urllib2
import json

while True:
    ip = input("What is your target IP: ")
    url = f"http://ip-api.com/json/{ip}"
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)

    print("IP: " + values["query"])
    print("City: " + values["city"])
    print("ISP: " + values["isp"])
    print("Country: " + values["country"])
    print("Region: " + values["region"])
    print("Timezone: " + values["timezone"])
    break



import urllib.request
import urllib.parse
import urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    adress = input ('Enter your location')
    if len(adress) < 1:
        break

    url = serviceurl+urllib.parse.urlencode({'adress':adress})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data=uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try: 
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("===Failure to retrieve ===")
        print(data)
        continue

lat= js ["results"][0]["geometry"]["location"]["lat"]
lng= js ["results"][0]["geometry"]["location"]["lng"]
print('lat',lat, 'lng', lng)
location = js['reuslts'][0]['formated_adress']
print(location)

# P6G01

import requests

base_url = requests.get('https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=ac1fbe548edb4eb2bf8f5642519ac399')
print("resp.text:\n", base_url.text[:300])
import requests
import math
def ficheiro():
    lst=[]
    with open ('categories.txt','r') as details:
        for l in details:
            line=l.split('\n')
            line="".join(line)
            lst.append(line)
        

        # det={i for i in lst}
    return(lst)
coordinates= input('coordenadas separadas por "," -->')
coordinates=coordinates.split(",")
lat=coordinates[1]
lon=coordinates[0]
km=float(input('Quanto deseja viajar?(km)-->'))
radius=km*1000
url="https://api.geoapify.com/v2/places"

resp = requests.get("https://api.geoapify.com/v2/places")
category=ficheiro()[0]
dic=f'?categories={category}&filter=circle:{lon},{lat},{radius}&limit=30&apiKey=ac1fbe548edb4eb2bf8f5642519ac399'
print(f"{url+dic}")
response = requests.get(f"{url+dic}")
print(response.json())
# dados=[]
# for n in response.json():
#     dados.append(n)
for n in range(0,len(response.json()['features'])):
    name=response.json()['features'][n]['properties']['name']
    type=response.json()['features'][n]['properties']['datasource']['raw']['tourism']
    categories=response.json()['features'][n]['properties']['categories']
    print(categories)
    print(name, '(', type ,')')
    country=response.json()['features'][n]['properties']['country']
    print(country)
    city=response.json()['features'][n]['properties']['city']
    print(city)
    a=response.json()['features'][n]['properties']['lon']
    print(a)
    b=response.json()['features'][n]['properties']['lat']
    print(b)
    dist=math.sqrt((float(a)-float(lon))**2+(float(b)-float(lat))**2)
    print(dist,'km')

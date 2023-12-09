import requests
def ficheiro():
    lst=[]
    with open ('categories.txt','r') as details:
        for l in details:
            line=l.split('\n')
            line="".join(line)
            lst.append(line)
        

        # det={i for i in lst}
    return(lst)
lat=48.56
lon=26.31
url="https://api.geoapify.com/v2/places"

resp = requests.get("https://api.geoapify.com/v2/places")
category=ficheiro()[1]
dic=f'?categories={category}&filter=rect%3A{lat}%2C{lon}%2C{lat}%2C{lon}&limit=100&apiKey=ac1fbe548edb4eb2bf8f5642519ac399'
print(f"{url+dic}")
response = requests.get(f"{url+dic}")
print(response.json())

def ficheiro():
    lst=[]
    with open ('categories.txt','r') as details:
        for l in details:
            line=l.split('\n')
            line="".join(line)
            lst.append(line)
        

        det={i for i in lst}
    print(det)
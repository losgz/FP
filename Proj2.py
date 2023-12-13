# P6G01
import requests
import math


URL = "https://api.geoapify.com/v2/places"


def location(url, latitude, longitude, radius, categories):
    dic = f"?categories={categories}&filter=circle:{latitude},{longitude},{radius}&limit=50&apiKey=ac1fbe548edb4eb2bf8f5642519ac399"    
    response = requests.get(f"{url+dic}")   
    return response.json()


def distance(lat1, lon1, lat2, lon2):
    distance = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    return distance


def formated_location(URL, latitude, longitude, radius, categories):
    lst = []
    counter = 0
    for i in categories:
        all_info = location(URL, latitude, longitude, radius, i)
    all_info = all_info.get("features")
    if all_info==[]:
        print('Não há lugares deste tipo nas redondezas')
        return 0
    else:
        for i in all_info:
            info = i.get("properties")
            lat1 = info.get("lat")
            lon1 = info.get("lon")
            dist = distance(lat1, lon1, latitude, longitude)
            if not info.get("name"):
                continue
            tpl = (
                (info.get("name")),
                (info.get("country")),
                (info.get("city")),
                (f"{lat1:.2f}"),
                (f"{lon1:.2f}"),
                (dist),
                (info.get("postcode")),
                (info.get("street")),
                (info.get("formatted")),
            )
            counter += 1
            lst.append(tpl)
        return counter, lst


def sort_attractions(lst , x):
    null_verification=1
    for n in lst:
        if n[x]==None:
            
            null_verification=0        
    if null_verification == 1:           
        if x == 0:   
            lst.sort(key=lambda y: y[0])
        elif x == 1:
            lst.sort(key=lambda y: y[1])
        elif x == 2:
            lst.sort(key=lambda y: y[2])
        elif x == 3:
            lst.sort(key=lambda y: y[5])
    else:
        print('Não foi possível dar sort, api incompleta') 
    for i in lst:
        print(i)
    return lst


def avg_distance(lst):
    total = 0
    for i in lst:
        total += i[5]
    return total / len(lst)

def print_all(option, URL, latitude, longitude, radius, categories):
        try:
            x = formated_location(URL, latitude, longitude, radius, categories)
            if x != 0:
                sort_attractions(x[1], option)
                print(f"\nNumber of locations: {x[0]}")
                print(f"Average distance: {avg_distance(x[1]):.4f}")
        except:
            print("\nInvalid categories, see the valid categories below: \n")
            with open("categories.txt", "r") as f:
                for line in f:
                    print(line.strip())
            new_category=input("Insert the categories (split them with a comma): ").split(",")
            print_all(option, URL, latitude, longitude, radius, new_category)      

def main():
    print("Welcome to our program!")
    print("Based on your preference, we will show you the best attractions for you.")
    print("Do you want to sort the attractions by: \n[0]-Name \n[1]-Country\n[2]-City\n[3]-Distance\n")
    option = input("Choose an option: ")
    if not option.isdigit() or int(option) > 3 or int(option) < 0:
        print("\nInvalid input, please choose an option form 0 to 3.\n")
        main()
    else:
        option =  int(option)

    coordinates = input("Insert the latitude and longitude (split them with a comma): ").split(",")
    radius = int(input("Insert the radius(km): "))
    radius*=1000
    categories = input("Insert the categories (split them with a comma): ").split(",")
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])
    print_all(option, URL, latitude, longitude, radius, categories)


if __name__ == "__main__":
    main()

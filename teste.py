# P6G01

import requests

base_url = 'https://api.geoapify.com/v2/places?categories=commercial.supermarket&filter=rect%3A10.716463143326969%2C48.755151258420966%2C10.835314015356737%2C48.680903341613316&limit=20&apiKey=ac1fbe548edb4eb2bf8f5642519ac399'
def get_posts():
    """Get all posts."""

    response = requests.get(f"{base_url}/posts")
    print(response)
    if response.status_code == 200:
        print(response.json())
        return response.json()


def get_posts_by_user(userId,lon,lat):
    """Gets all posts of the user userId."""

    # Create a dictionary with key:value pairs to pass in the URL query string
    params = {'lat': lat}
    response = requests.get(f"{base_url}/posts", params=params)
    
        # The params= argument is encoded in the URL query string.

    print(response.request.url)  # Uncomment to see the constructed URL

    if response.status_code == 200:
        return response.json()  # decode JSON into a python object (list)


def add_post(title, body, user_id):
    """Add a new post."""

    # Create a dict with the data to send
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(f"{base_url}/posts", json=data)
        # With json=... the request content is sent as JSON

    if response.status_code == 201:
        return response.json()
lon=43.32
lat=86.32

def main():
    # Uncomment to see all posts
    print("\nTesting get_posts")
    posts = get_posts()
    print(posts, end="\n\n")

    print("\nTesting get_posts_by_user")
    some_posts = get_posts_by_user(1,lon,lat)
    print(some_posts)
    # Should return a list of dictionaries: 
    # [{'userId': 1, 'id': 1, 'title': 'sunt ...', 'body': 'quia ... '},
    #  {'userId': 1, 'id': 2, 'title': 'qui ...', 'body': 'est ...'}]

    print("\nTesting add_post")
    added = add_post("A title", "Some content\nMore interesting content", 5)
    print(repr(added))


if __name__ == "__main__":
    main()

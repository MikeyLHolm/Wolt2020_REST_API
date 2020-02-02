# 200 – OK. The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
# 204 – No Content. The server successfully processed the request and did not return any content.
# 301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
# 400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).
# 401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.
# 403 – Forbidden. Access to the specified resource is denied.
# 404 – Not Found. The requested resource was not found on the server.
# 500 – Internal Server Error. Occurs when an unknown error has occurred on the server.

# import requests
# import json
#
# response = requests.get('https://github.com/woltapp/summer2020/blob/master/restaurants.json')
# if response.status_code != 200:
#     print("Something went wrong")
#     print(response)
# else:
#     print("Request is successful.")
#     print(response)
# print(type(response.json()))

# list comprehension

import requests
import json
import geopy.distance

restaurant_data = None

with open('restaurants.json') as json_file:
    restaurant_data = json.load(json_file)

# name, description and tags
query_coords = (24.9695, 60.1775)
query_name = "Happy Waffle Helsinki"
query_description = "Tuoretta ja herkullista ruokaa"
query_tags = "pizza"

# Expression for item in list


def check_distance(q_coords, location):
    if geopy.distance.distance(q_coords, location).km < 3:
        return 1
    else:
        return 0


# Check if location is within 3km radius of the query_location.
result = [item for item in restaurant_data['restaurants'] if check_distance(query_coords, item['location'])]

# Find out if query matches: name, description and tags
for restaurant in result:
    if restaurant['tags'][0] == query_tags:
        print(restaurant['name'])
    elif restaurant['tags'][1] == query_tags:
        print(restaurant['name'])

# print(restaurant['name'])


# for item in restaurant_data['restaurants']:
#     # if check_distance(query_coords, item['location']):
#     #     print(item['name'])
#     if check_distance(query_coords, item['location']) and item['name'] == query_name:
#         print(item['name'])
#     if check_distance(query_coords, item['location']) and item['description'] == query_description:
#         print(item['name'])
#     if check_distance(query_coords, item['location']) and item['tags'] == query_tags:
#         print(item['name'])





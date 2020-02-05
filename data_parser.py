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

import json
import geopy.distance

# COMMENTS:
# add case sensitivity to Name and description!!
# ideally i would try to do do everything in one simple loop using list comprehension. If that is possible.


def query(q, lat, lon):
    with open('restaurants.json') as json_file:
        restaurant_data = json.load(json_file)
    q_coords = (lat, lon)
    print("Query =", q)
    print("Query coordinates", q_coords)
    # Check if location is within 3km radius of the query_location.
    # r = [item for item in restaurant_data['restaurants'] if check_distance(q_coords, item['location']) is True]
    # return_data_list = []
    # Find out if query matches: name, description or tags
    # for restaurant in r:
    #     sw = 0
    #     # print(restaurant['description'])
    #     # print(type(restaurant['description']))
    #     # print(q)
    #     # print(type(q))
    #     # print(check_tags(q, restaurant['tags']) is True)
    #     # print(restaurant['name'])
    #     if restaurant['description'].find(q) != -1:
    #         print("test2", restaurant['name'])
    #         sw = 1
    #     if restaurant['name'].find(q) != -1:
    #         print("test1", restaurant['name'])
    #         sw = 1
    #     # elif restaurant['description'].find(q) != -1:
    #     #     print("test2")
    #     if check_tags(q, restaurant['tags']) is True:
    #         print("q found at " + restaurant['name'])
    #         sw = 1
    #     if sw == 0:
    #         print("Deleting " + restaurant['name'])
    #         del restaurant
    #     print(r)
    #
    # # remove duplicates from the list
    # # return_data_list = list(dict.fromkeys(return_data_list))
    # # print(return_data_list)
    #
    # # sort list alphabetically
    # # return_data_list.sort()
    # # print(return_data_list)
    for restaurant in restaurant_data['restaurants']:
        if check_distance(q_coords, restaurant['location']) is False:
            del restaurant_data
        elif parse_fields(q, restaurant) is False:
            del restaurant_data
        #         print("test2", restaurant['name'])
        #         sw = 1
        #     if restaurant['name'].find(q) != -1:
        #         print("test1", restaurant['name'])
        #         sw = 1
        #     # elif restaurant['description'].find(q) != -1:
        #     #     print("test2")
        #     if check_tags(q, restaurant['tags']) is True:
        #         print("q found at " + restaurant['name'])
        #         sw = 1
        #     if sw == 0:
        #         print("Deleting " + restaurant['name'])
        #         del restaurant
    with open('results.json', 'w') as f:
        json.dump(restaurant_data, f, indent=2)
    print("Results printed to results.json")


# Comparing query to the restaurant_data in json file.
def parse_fields(query, restaurant):
    sw = 0
    if restaurant['description'].find(query) != -1:
        sw = 1
    if restaurant['name'].find(query) != -1:
        sw = 1
    if check_tags(query, restaurant['tags']) is True:
        sw = 1
    if sw == 0:
        return False
    else:
        return True


# function that returns 1 if q can be found from tags.
def check_tags(q, tags):
    for i in tags:
        if i.find(q) != -1:
            return True
    return False


# function to check if location is sub 3km from the restaurant.
def check_distance(q_coords, location):
    if geopy.distance.distance(q_coords, location).km < 3:
        return True
    else:
        return False


q = "izz"
lat = 24.9695
lon = 60.1775
query(q, lat, lon)

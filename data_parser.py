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


# restaurant_data = None
def query(q, lat, lon):
    with open('restaurants.json') as json_file:
        restaurant_data = json.load(json_file)

    q_coords = (lat, lon)
    # Check if location is within 3km radius of the query_location.
    r = [item for item in restaurant_data['restaurants'] if check_distance(q_coords, item['location'])]

    # return_data_list = []
    print(len(r), "\n")

    # Find out if query matches: name, description or tags
    # probably should change 'tags' to iterating thru list instead fixed 0 & 1.
    for restaurant in r:
        if any(item for item in restaurant['tags'] if q in item):
            print("q found at " + restaurant['name'])
            continue
        # elif q in restaurant['tags'][1]:
        #     return_data_list.append(restaurant['name'])
        elif q in restaurant['name']:
            print("test1")
            continue
            # return_data_list.append(restaurant['name'])
        elif q in restaurant['description']:
            print("test2")
            continue
            # return_data_list.append(restaurant['name'])
        else:
            print("Deleting " + restaurant['name'])
            r.remove(restaurant)
    print(len(r), "\n")
    print(r)

    # remove duplicates from the list
    # return_data_list = list(dict.fromkeys(return_data_list))
    # print(return_data_list)

    # sort list alphabetically
    # return_data_list.sort()
    # print(return_data_list)

    with open('results.json', 'w') as f:
        json.dump(r, f, indent=2)


# placeholder query variables.
# query_c = (24.9695, 60.1775)
# q_input = "burg"

# Expression for item in list


# function to check if location is sub 3km from the restaurant.
def check_distance(q_coords, location):
    if geopy.distance.distance(q_coords, location).km < 3:
        return 1
    else:
        return 0

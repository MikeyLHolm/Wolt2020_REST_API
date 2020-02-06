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

    ret = [item for item in restaurant_data['restaurants'] if query_filter(q, q_coords, item) is True]


    with open('results.json', 'w') as f:
        json.dump(ret, f, indent=2)
    print("Results printed to results.json")

    return ret

# Main function to parse thru the json data with search values
def query_filter(query, q_coords, restaurant):
    sw = 0
    dist = 0
    if check_distance(q_coords, restaurant['location']) is True:
        dist = 1
    if restaurant['description'].find(query) != -1:
        sw = 1
    if restaurant['name'].find(query) != -1:
        sw = 1
    if check_tags(query, restaurant['tags']) is True:
        sw = 1
    if sw == 1 and dist == 1:
        return True
    else:
        return False


# function that returns 1 if q can be found from tags.
def check_tags(q, tags):
    for i in tags:
        if i.find(q) != -1:
            return True
    return False


# Check if location is within 3km radius of the query_location.
def check_distance(q_coords, location):
    if geopy.distance.distance(q_coords, location).km < 3:
        return True
    else:
        return False


# q = "izz"
# lat = 24.9695
# lon = 60.1775
# query(q, lat, lon)

import json
import geopy.distance


# Open file and parse through using list comprehension while checking if query variables match.
def query(q, lat, lon):
    with open('restaurants.json') as json_file:
        restaurant_data = json.load(json_file)
    q_coords = (lon, lat)
    ret = [item for item in restaurant_data['restaurants'] if query_filter(q, q_coords, item) is True]

    return ret


# Main function to parse through the json data with search values
def query_filter(query, q_coords, restaurant):
    switch = 0
    dist = 0
    description = restaurant['description'].lower()
    name = restaurant['name'].lower()
    if check_distance(q_coords, restaurant['location']) is True:
        dist = 1
    if description.find(query) != -1:
        switch = 1
    if name.find(query) != -1:
        switch = 1
    if check_tags(query, restaurant['tags']) is True:
        switch = 1
    if switch == 1 and dist == 1:
        return True
    else:
        return False


# Returns True if query can be found from tags.
def check_tags(q, tags):
    for i in tags:
        if i.find(q) != -1:
            return True
    return False


# Returns True if restaurant location is within 3km radius of the query_location.
def check_distance(q_coords, location):
    if geopy.distance.distance(q_coords, location).km < 3:
        return True
    else:
        return False

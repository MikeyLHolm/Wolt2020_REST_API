import requests
lat = 60.1775
lon = 24.9695
q = "pizza"

# Alternate way of formatting:
# response = requests.get(f"http://127.0.0.1:5000/restaurants/search?q={q}&lat={lat}&lon={lon}")

# For manually testing response codes:
response = requests.get("http://127.0.0.1:5000/restaurants/search?q=pizza&lat=24.9695&lon=60.1775")

if response.status_code == 200:
    print("\nResponse code =",response.status_code)
else:{
    print("204 – No Content. The server successfully processed the request and did not return any content.\n"
    "301 – Moved Permanently. The server responds that the requested page (endpoint) has been moved to another address\n"
    "      and redirects to this address.\n"
    "400 – Bad Request. The server cannot process the request because the client-side errors (incorrect request format).\n"
    "401 – Unauthorized. Occurs when authentication was failed, due to incorrect credentials or even their absence.\n"
    "403 – Forbidden. Access to the specified resource is denied.\n"
    "404 – Not Found. The requested resource was not found on the server.\n"
    "500 – Internal Server Error. Occurs when an unknown error has occurred on the server.\n"
    "\nResponse code =",response.status_code)
    }

# print(ret.json())



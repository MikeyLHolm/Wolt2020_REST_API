# What is this project?
A REST API endpoint that allows searching restaurants.
Originally done for [Wolt's](https://wolt.com/) Summer 2020 Internship Engineering Backend Pre-assignment.

API needs to accept three parameters (query string, latitude and longitude) and should return restaurant(s) (objects) which match the given query string and are closer than 3 kilometers from coordinates.

Detailed instructions:
https://github.com/woltapp/summer2020

## My solution

* I chose **Python** as I'm interested in *Machine learning* and *all things AI* where Python is greatly used and I had already planned on learning the language. 
* Using Flask with Python I can create a development server to run the queries at.
* One larger function (query_filter) passed into list comprehension as a condition filters query-matching restaurants into a new list which is returned as a file in repo root and as a .json type list to the web address.
* Trying to improve user xp with various error messages and instructions.

## How to use?

This API requires [Python3](https://realpython.com/installing-python/) to use.

### Download:
```git clone https://github.com/MikeyLHolm/Wolt2020_REST_API.git```

### Launch REST API in terminal:
```python3 rest_api.py```

### How to search?

After launching the program in terminal you can use it in either a terminal or in a browser.

#### Terminal
Start by running:

```curl http://127.0.0.1:5000```

Typical search in terminal would look something like:

```curl http://127.0.0.1:5000/restaurants/search?q=sushi&lat=60.1775&lon=24.9695```

* q: query string. Full or partial match for the string is searched from name, description and tags fields. A minimum length for the query string is one character.
* lat: latitude coordinate
* lon: longitude coordinate

#### Browser
Typical search in a browser, above rules apply here also:

http://127.0.0.1:5000/restaurants/search?q=sushi&lat=60.1775&lon=24.9695

### Required libraries:

To install a library: pip3 install libraryname
* flask
* geopy
* json
* jsonify
* request

### Shutting down flask
Terminal:

```curl http://127.0.0.1:5000/shutdown```

Browser:

http://127.0.0.1:5000/shutdown

### Want to get your results into a .json file?

For checking if file already exists, you need to install *os*-library.

Add following code to *line 22* in rest_api.py (this will delete results.json from repo root if you have one already):

```
try:
    os.remove('results.json')
except OSError:
    pass
```
and following code to *line 31* in data_parser.py (creates results.json and copies the return data into the file):

```
with open('results.json', 'w') as f:
    json.dump(ret, f, indent=2)
```

Your code should look something like:
![rest_api](/images/line22.png)
![data_parser](/images/line31.png)

## What is REST API?

>Let’s say you’re trying to find videos about Batman on Youtube. You open up Youtube, type “Batman” into a search field, hit enter, and you see a list of videos about Batman. A REST API works in a similar way. You search for something, and you get a list of results back from the service you’re requesting from.
>
>An API is an application programming interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.
>
>REST determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.
>
>Each URL is called a request while the data sent back to you is called a response.

Zell Liew @ www.smashingmagazine.com 

## Links:

[Understanding And Using REST APIs](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)

[What is REST](https://en.wikipedia.org/wiki/Representational_state_transfer)

[My Linkedin](https://www.linkedin.com/in/mlindholm3)

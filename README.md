# Wolt_backend_pre_assignment
Summer 2020 Internships - Engineering Backend Pre-assignment

## Option 2) Backend task - search
Create a REST API endpoint that allows searching restaurants. API needs to accept three parameters:

q: query string. Full or partial match for the string is searched from name, description and tags fields. A minimum length for the query string is one character.
lat: latitude coordinate (customer's location)
lon : longitude coordinate (customer's location)
API should return restaurant (objects) which match the given query string and are closer than 3 kilometers from coordinates.

Example query:

/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
This search would return restaurants (in JSON format) which contain a word sushi and are closer than 3km to the point [60.17045, 24.93147].

Please do not use any on-disk database (MySQL, PostgreSQL, ...) or ElasticSearch in this assignment. The task can be completed without them.

https://jobs.lever.co/wolt/7d18a18f-1a28-48a6-ab69-a17327466675

https://github.com/woltapp/summer2020

## My solution

## How to use?

This API requires [Python3](https://realpython.com/installing-python/) to use.

### Download:
```git clone https://github.com/MikeyLHolm/Wolt2020_REST_API.git```

### Open up a new prompt to test out the API using curl.
```curl http://127.0.0.1:5000/```

### Required libraries:

To install a library: pip3 install libraryname
* flask
* geopy
* json
* jsonify
* os
* request

## What is REST API?

Let’s say you’re trying to find videos about Batman on Youtube. You open up Youtube, type “Batman” into a search field, hit enter, and you see a list of videos about Batman. A REST API works in a similar way. You search for something, and you get a list of results back from the service you’re requesting from.

An API is an application programming interface. It is a set of rules that allow programs to talk to each other. The developer creates the API on the server and allows the client to talk to it.

REST determines how the API looks like. It stands for “Representational State Transfer”. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called a resource) when you link to a specific URL.

Each URL is called a request while the data sent back to you is called a response.

## Links:

[What is REST](https://en.wikipedia.org/wiki/Representational_state_transfer)

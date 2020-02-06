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

## How to use?

##### Required libraries:
*json
*geopy
*os
*flask
*jsonify
*request

 
 curl http://127.0.0.1:5000/

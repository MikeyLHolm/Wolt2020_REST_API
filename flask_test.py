# If flask stuck running:
# $ ps -fA | grep python
# 501 81651 12648   0  9:53PM ttys000    0:00.16 python -m SimpleHTTPServer
# kill 81651
from data_parser import query
from flask import Flask, jsonify, request      #import objects from the Flask model
app = Flask(__name__)   #define app using Flask


@app.route("/restaurants/search")
def search():

    q = request.args.get('q')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    query(q, lat, lon)
    # print("Please enter search parameterssss    ")

    return '''  query is : {}
                lat : {}
                lon is : {}'''.format(q, lat, lon)


@app.route("/restaurants", methods=['GET'])
def test():
    return jsonify({'helpful message': 'Woah it kinda works!'})


# def testi(q, lat):
#     if q == "pizza":
#         print("pizza be good\n")
#     else:
#         print("sorry, not pizza")
#     print(lat)


if __name__ == "__main__":
    app.run(debug=True, port=5000)


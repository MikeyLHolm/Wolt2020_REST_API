from data_parser import query
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/restaurants/search")
def search():

    q = request.args.get('q')
    if len(q) == 0:
        return "A minimum length for the query string is one character."
    if q.isupper() is True:
        q = q.lower()
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    ret = query(q, lat, lon)

    if not ret:
        return "No results found with search parameters"
    else:
        return jsonify(ret), 200


@app.route("/", methods=['GET'])
def instructions():
    return """instructions:
    
    typical search: http://127.0.0.1:5000/restaurants/search?q=sushi&lat=60.1775&lon=24.9695
    
    q: query string. Full or partial match for the string is searched from name, description and tags fields.
              A minimum length for the query string is one character. 
                 
    lat: latitude coordinate
            
    lon: longitude coordinate
    
    exit: http://127.0.0.1:5000/shutdown
    """


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


# Change debug=False to debug=True to run in debug mode.
if __name__ == "__main__":
    app.run(debug=True, port=5000)


# test...

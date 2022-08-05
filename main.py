import db_connection.py
From flask  import Flask, request, Response
import json

app =Flask(__name__)

@app.route('/')
def index():
    return "Hello ...Welcome to Productivity App"

@app.route('/item/new', methods=['POST'])
def insert_new_task():
    req_data = request.get_json()
    item = req_data['item']
    
    res_data = db_connection.connect_db(Productivity)
    
    # return 400 status if item is not added (error)
    
    if res_data is None:
        response = Response("{'error': 'No item added - " + item + "'}", status=400, mimetype='application/json') 
        return response
    
    #json.dumps to convert python into JSON object
    response = Response(json.dumps(res_data), mimetype='application/json')
 
 return response
 
 @app.route('/items/all')
def retrieve_items():
    # Get items from the db connection file 
    res_data = db_connection.retrieve_items()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response
 
 
 def retrieve_items():
    try:
        # Code below to be checked with mysql instead of mysql:
        # conn = sqlite3.connect(DB_PATH)
        # c = conn.cursor()
        # c.execute('select * from items')
        # rows = c.fetchall()
        # return { "count": len(rows), "items": rows }
     except Exception as e:
        print('Error: ', e)
        return None

# Function below to retrieve INDIVIDUAL items:

@app.route('/item/status', methods=['GET'])
def retrieve_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the db_connection file
    status = db_connection.retrieve_item(item_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'No item added - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response
       
    

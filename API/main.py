from flask import Flask, jsonify, request # Added render_template for HTML file
import API.db_connection as db_connection
import json

user_points = 0

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html') # Links to base.html file in "Templates" directory

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
 
 
def retrieve_task():
    try:
        # Code below to be checked with mysql instead of mysql:
        conn = _connect_to_db('Productivity')
        c = conn.cursor()
        c.execute('select * from task')
        result = c.fetchall()
        return { "count": len(result), "task": result }
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
    
    # PUT method to execute the Update_priority function 
    
@app.route('/item/update', methods=['PUT'])
def update_priority():
    # Get item from the POST body
    req_data = request.get_json()
    task = req_data['task']
    priority = req_data['priority']

    # Update priority of item in the list:
    res_data = db_connection.update_status(task, priority)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

# DELETE request:

@app.route('/item/remove', methods=['DELETE'])
def delete_task():
    # Get item from the POST body
    req_data = request.get_json()
    task = req_data['Task']

    # Delete item from the list
    res_data = db_connection.delete_task(task)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting task - '" + task +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    
    #Adding points to the user for completion of task
    user_points += 1




       
    

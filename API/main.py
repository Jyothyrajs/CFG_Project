from flask import Flask, jsonify, request # Added render_template for HTML file
import API.db_connection as dbconnection
import json

#Starting User Points
user_points = 0

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html') # Links to base.html file in "Templates" directory

@app.route('/tasks/new', methods=['POST'])
def insert_new_task():
    req_data = request.get_json()
    item = req_data['Task']
    
    res_data = dbconnection.connect_db(Productivity)
    
    # return 400 status if task is not added (error)
    
    if res_data is None:
        response = Response("{'error': 'No task added - " + Task + "'}", status=400, mimetype='application/json') 
        return response
    
    #json.dumps to convert python into JSON object
    response = Response(json.dumps(res_data), mimetype='application/json')
 
    return response
 
@app.route('/tasks/all')
def retrieve_tasks():
    # Get items from the db connection file 
    res_data = dbconnection.retrieve_tasks()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response
 
 
def retrieve_task():
    try:
        # Code below to be checked with mysql instead of mysql:
        conn = dbconnection('Productivity')
        c = conn.cursor()
        c.execute('select * from Task')
        result = c.fetchall()
        return { "count": len(result), "Task": result }
    except Exception as e:
        print('Error: ', e)
        return None

# Function below to retrieve INDIVIDUAL items:

@app.route('/tasks/status', methods=['GET'])
def retrieve_task():
    # Get parameter from the URL
    task_name = request.args.get('Task')

    # Get items from the db_connection file
    status = dbconnection.retrieve_task(task_name)

    # Return 404 if item not found
    if status is None:
        response = Response("{'error': 'No task added - %s'}"  % task_name, status=404 , mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response
    
    # PUT method to execute the Update_priority function 
    
@app.route('/tasks/update', methods=['PUT'])
def update_priority():
    # Get item from the POST body
    req_data = request.get_json()
    task = req_data['Task']
    priority = req_data['Priority']

    # Update priority of item in the list:
    res_data = dbconnection.update_status(Task, Priority, Duration)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating task - '" + Task + ", " + Status + ", " + Duration + "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

# DELETE request:

@app.route('/task/remove', methods=['DELETE'])
def delete_task():
    # Get item from the POST body
    req_data = request.get_json()
    task = req_data['Task']

    # Delete item from the list
    res_data = dbconnection.delete_task(Task)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting task - '" + Task +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    
    #Adding points to the user for completion of task
    user_points += 1




       
    

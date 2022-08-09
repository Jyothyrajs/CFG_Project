import mysql.connector
from config import HOST,USER,PASSWORD

class DbConnectionError(Exception):
    pass


#NOTSTARTED = 'Not Started'
#INPROGRESS = 'In Progress'
#COMPLETED = 'Completed'


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name)
    return cnx
    

def insert_new_task(Task,Priority,duration):
    try:
        project_db = connect_db('Productivity')
        cur = project_db.cursor()
        query = """
                   INSERT INTO TODO_LIST(Task, Priority, deadline)
                   VALUES("{}", "{}", "{}")'.format(Task, Priority, deadline) 
                   """ #Ive seen some people use %s to indicate that its a string that should be inputted, butis priority and deadline a string? 
        cur.execute(query)

    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()
            print("DB connection closed")

# UPDATE priority level of to do list item (e.g. high priority) 

def update_priority(task, priority): 
    # Check if the passed status is a valid value
    if (priority.lower().strip() == 'High'):
        status = NOTSTARTED
    elif (priority.lower().strip() == 'Medium'):
        status = INPROGRESS
    elif (priority.lower().strip() == 'Low'):
        status = COMPLETED
    else:
        print("Error: Status invalid " + status)
        return None

     try: 
        project_db=connect_db('Productivity')
        cur = project_db.cursor()
        cur.execute("""Update Task 
                       set status= %s 
                       where item= %s""",(status, task)) #should this be priority insteead of status? Not sure  
        conn.commit() #Got up to here with editing. 
        return {task: status}
 except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()
        return None

def delete_task(task):
    # Below needs adapting to mysql:
#     try:
#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         c.execute('delete from items where item=?', (item,))
#         conn.commit()
#         return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None
 

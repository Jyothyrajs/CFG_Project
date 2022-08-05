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




def insert_new_task(Task,Priority,duration,deadline):
    try:
        project_db = connect_db('Productivity')
        query = "INSERT INTO TODO_LIST(Task,Priority,duration,deadline) VALUES('Task,Priority,duration,deadline')'"
        my_cursor = project_db.cursor()
        my_cursor.execute(query)

    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()

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
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where item=?', (status, item))
        conn.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None

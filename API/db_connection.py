import mysql.connector
from config import HOST,USER,PASSWORD

class DbConnectionError(Exception):
    pass


# NOTSTARTED = 'Not Started'
# INPROGRESS = 'In Progress'
# COMPLETED = 'Completed'


def _connect_to_db(db_name):
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name)
    return conn


def insert_new_task(Task,Priority,Duration):
    try:
        project_db = _connect_to_db('Productivity')
        cur = project_db.cursor()
        query = """
                   INSERT INTO TODO_LIST(Task, Priority, Duration)
                   VALUES("{}", "{}", "{}")'.format(Task, Priority, Duration) 
                   """ #Ive seen some people use %s to indicate that its a string that should be inputted, butis priority and deadline a string? 
        cur.execute(query)

    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()
            print("DB connection closed")

# UPDATE priority level of to do list item (e.g. high priority) 

def update_priority(Task, Priority): 
    # Check if the passed status is a valid value
    if (Priority.lower().strip() == 'High'):
        Priority = NOTSTARTED
    elif (Priority.lower().strip() == 'Medium'):
        Priority = INPROGRESS
    elif (Priority.lower().strip() == 'Low'):
        Priority = COMPLETED
    else:
        print("Error: Status invalid " + Priority)
        return None

     try: 
        project_db=_connect_to_db('Productivity')
        cur = project_db.cursor()
        cur.execute("""Update Task 
                       set status= %s 
                       where task= %s""",(Priority, Task))
        conn.commit()
        return {Task: Priority}

 except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()
        return None

def delete_task(Task):
    # Below needs adapting to mysql:?
    try:
        project_db=_connect_to_db('Productivity')
        cur = project_db.cursor()
        query= """Delete From TODO_LIST Task Where Task =%s"""
        cur.execute(query)
        return {'task': Task}

except Exception:
    raise DbConnectionError("Unable to connect to database")
finally:
    if project_db:
        project_db.close()
    print("DB connection closed")
        return None


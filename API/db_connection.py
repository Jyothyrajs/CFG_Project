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


def insert_new_task(Task,Priority,duration):
    try:
        project_db = _connect_to_db('Productivity')
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
        priority = NOTSTARTED
    elif (priority.lower().strip() == 'Medium'):
        priority = INPROGRESS
    elif (priority.lower().strip() == 'Low'):
        priority = COMPLETED
    else:
        print("Error: Status invalid " + priority)
        return None

     try: 
        project_db=_connect_to_db('Productivity')
        cur = project_db.cursor()
        cur.execute("""Update Task 
                       set status= %s 
                       where item= %s""",(priority, task))
        conn.commit()
        return {task: priority}

 except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()
        return None

def delete_task(task):
    # Below needs adapting to mysql:?
    try:
        project_db=_connect_to_db('Productivity')
        cur = project_db.cursor()
        query= """Delete From TODO_LIST Task Where Task =%s"""
        cur.execute(query)
        return {'task': task}

except Exception:
    raise DbConnectionError("Unable to connect to database")
finally:
    if project_db:
        project_db.close()
    print("DB connection closed")
        return None


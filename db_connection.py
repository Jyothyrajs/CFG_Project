import mysql.connector
from config import HOST,USER,PASSWORD


#NOTSTARTED = 'Not Started'
#INPROGRESS = 'In Progress'
#COMPLETED = 'Completed'


def connect_db(db_name):
    context = mysql.connector.connect(host=HOST,
                                      user=USER,
                                      password=PASSWORD,
                                      database=db_name)
    return context



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

from asyncio import tasks


user_tasks = []
def add_task(task):
    user_tasks.append(task)
    print(user_tasks)

# class TodoList:
#     def __init__(self):
#         tasks = []

#     def add_task(task):
#         tasks.append(task)

#     def list_tasks():
#         print(tasks)
#         return tasks

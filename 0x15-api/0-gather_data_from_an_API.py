#!/usr/bin/python3
"""Request employee ID from API
"""
import requests
import sys

def get_todo_list_progress(employee_id):
    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user = user_response.json()

    # Fetch tasks data
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    tasks = tasks_response.json()

    # Filter completed tasks
    tasks_completed = [task for task in tasks if task['completed']]

    # Log employee TODO list progress
    print(f'Employee {user["name"]} is done with tasks({len(tasks_completed)}/{len(tasks)}):')

    # Log completed task titles
    for task in tasks_completed:
        print(f'\t {task["title"]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_api <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)

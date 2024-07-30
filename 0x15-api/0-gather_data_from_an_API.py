#!/usr/bin/python3
"""using the JSONPlaceholder API:
   returns information about the TODO list progress for a given employee ID"""
import requests

def get_todo_list_progress(employee_id):
    url = f"(link unavailable)"
    response = requests.get(url)
    data = response.json()

    employee_name = data["employee_name"]
    total_tasks = len(data["todos"])
    completed_tasks = [task for task in data["todos"] if task["completed"]]
    num_done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_todo_list_progress(employee_id)

#!/usr/bin/python3
""" script that gathers data from an api """

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.
    """

    name_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")

    if name_response.status_code != 200:
        print(f"Error fetching employee with ID {employee_id}. Status code: {name_response.status_code}")
        sys.exit(1)

    name_data = name_response.json()

    if not name_data:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = name_data['name']

    # Fetch all todos for the employee
    todos_response = requests.get
    (f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if todos_response.status_code != 200:
        print (f"Error fetching TODO list for employee with ID {employee_id}. Status code: {todos_response.status_code}")
        sys.exit(1)

    todos_data = todos_response.json()

    # Filter completed todos
    completed_todos = [todo for todo in todos_data if todo['completed']]

    # Prepare and print task list
    print (f"Employee {employee_name} is done with tasks ({len(completed_todos)}/{len(todos_data)}):")
    for todo in completed_todos:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)

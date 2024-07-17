#!/usr/bin/python3
""" Python script to export data in the JSON format """

import json
import requests
import sys


def get_employeeprogress(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error fetching user with ID {employee_id}")
        return None, None

    data = user_response.json()
    employee_name = data.get('username')

    todos_request = requests.get(f"{url}/todos?userId={employee_id}")
    if todos_request.status_code != 200:
        print(f"Error fetching TODO list for user with ID {employee_id}")
        return None, None

    todolist_data = todos_request.json()
    total_tasks = len(todolist_data)
    complete_tasks = [task for task in todolist_data if task.get('completed')]
    total_number_of_tasks = len(complete_tasks)

    employee_tasks = []
    for task in todolist_data:
        list_info = {
            "username": employee_name,
            "task": task.get('title'),
            "completed": task.get('completed')
        }
        employee_tasks.append(list_info)

    return employee_name, employee_tasks


def export_list():
    url_sec = "https://jsonplaceholder.typicode.com"
    list_of_employee_tasks = {}

    for employee_id in range(1, 11):
        employee_name, tasks = get_employeeprogress(employee_id)
        if employee_name and tasks:
            list_of_employee_tasks[employee_id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(list_of_employee_tasks, f, indent=2)


if __name__ == "__main__":
    export_list()

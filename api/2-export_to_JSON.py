#!/usr/bin/python3
""" script that gathers data from an api """

import json
import requests
import sys


def get_employeeprogress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"

    user_request = requests.get("{}/users/{}".format(url, employee_id))
    if user_request.status_code != 200:
        print("Error fetching user with ID {}".format(employee_id))
        return

    data = user_request.json()
    employee_name = data.get('name')
    username = data.get('username')

    todos_request = requests.get("{}/todos?userId={}".format(url, employee_id))
    if todos_request.status_code != 200:
        print("Error fetching TODO list for user with ID {}"
              .format(employee_id))

    todolist_data = todos_request.json()
    total_tasks = len(todolist_data)
    complete_tasks = [task for task in todolist_data if task.get('completed')]
    total_number_of_tasks = len(complete_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_number_of_tasks, total_tasks))

    for task in complete_tasks:
        print(f"\t {task.get('title')}")

    tasks = [{"task": task.get('title'),
              "completed": task.get('completed'),
              "username": username} for task in todolist_data]

    jsondata = {str(employee_id): tasks}

    with open("{}.json".format(employee_id), 'w') as jsonfile:
        json.dump(jsondata, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employeeprogress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID")

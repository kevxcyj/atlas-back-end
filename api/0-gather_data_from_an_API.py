#!/usr/bin/python3
""" script that gathers data from an api """

import requests
import sys


def get_employeeprogress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get("{}/users/{}".format(url, employee_id))
    if user_response.status_code != 200:
        print("Error fetching user with ID {}".format(employee_id))
        return

    data = user_response.json()
    employeename = data.get('name')
    todolist_request = requests.get("{}/todos?userId={}"
                                  .format(url, employee_id))
    
    if todolist_request.status_code != 200:
        print("Error fetching TODO list for user with ID {}"
              .format(employee_id))

    todolist_data = todolist_request.json()
    total_tasks = len(todolist_data)
    complete_tasks = [task for task in todolist_data if task.get('completed')]
    total_number_of_tasks = len(complete_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employeename, total_number_of_tasks, total_tasks))

    for task in complete_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employeeprogress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID")

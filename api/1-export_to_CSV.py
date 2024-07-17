#!/usr/bin/python3
""" script that gathers data from an api """

import csv
import requests
import sys


def get_employeeprogress(employee_id):
    url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(url, employee_id))
    if user_response.status_code != 200:
        print("Error fetching user with ID {}".format(employee_id))
        return

    data = user_response.json()
    username = data.get('username')
    print("User ID: {}, Username: {}".format(employee_id, username))

    todos_request = requests.get("{}/todos?userId={}"
                                  .format(url, employee_id))
    if todos_request.status_code != 200:
        print("Error fetching TODO list for user with ID {}"
              .format(employee_id))
        return

    todolist_data = todos_request.json()
    total_tasks = len(todolist_data)
    complete_tasks = [task for task in todolist_data if task.get('completed')]
    total_number_of_tasks = len(complete_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(username, total_number_of_tasks, total_tasks))

    for task in complete_tasks:
        print("\t {}".format(task.get('title')))

    with open("{}.csv".format(employee_id), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todolist_data:
            writer.writerow([employee_id, username, task.get('completed'),
                             task.get('title')])

    with open("{}.csv".format(employee_id), mode='r') as file:
        reader = csv.reader(file)
        csv_task  = sum(1 for row in reader)
        if csv_task != total_tasks:
            print("Warning: Number of tasks in CSV ({}) does not match the "
                  "expected count ({}).".format(csv_task, total_tasks))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employeeprogress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID")

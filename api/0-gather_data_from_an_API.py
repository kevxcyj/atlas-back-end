#!/usr/bin/python3
""" script that gathers data from an api """

import requests
import sys


import requests
from sys import argv


def get_employee_todos(employee_id):
    """ Employee ID """

    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todo = requests.get(site + "todos?userId={}".format(employee_id))

    users = user.json()
    names = users.get("name")
    todos = todo.json()

    completed = [i for i in todos if i.get("completed")]
    all_todos = len(todos)
    done_todos = len(completed)

    print("Employee {} is done with tasks({}/{}):"
          .format(names, done_todos, all_todos))

    for i in completed:
        print("\t {}".format(i.get("title")))


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])
#!/usr/bin/python3
""" script that gathers data from an api """

import csv
import requests
from sys import argv


def get_employee_todos(employee_id):
    """ Employee ID """

    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todo = requests.get(site + "todos?userId={}".format(employee_id))

    users = user.json()
    usernames = users.get("username")
    todos = todo.json()
    csv_file_name = "{}.csv".format(employee_id)

    completed = [i for i in todos if i.get("completed")]

    for i in completed:
        print("\t {}".format(i.get("title")))

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([employee_id, usernames,
                             i.get('completed'), i.get('title')])


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])

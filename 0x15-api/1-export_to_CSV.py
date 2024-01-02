#!/usr/bin/python3
"""get data from jsonplaceholder api"""

import csv
import requests
import sys


if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(todos_url, params={'userId': sys.argv[1]}).json()
    users_url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(f"{users_url}/{sys.argv[1]}").json()
    complete_tasks = [
        task.get("title") for task in tasks if task.get("completed")
    ]
    name = user.get("name")
    done = f'{len(complete_tasks)}/{len(tasks)}'
    print(
        f"Employee {name} is done with tasks({done}):"
    )
    for task in complete_tasks:
        print(f'\t {task}')

    with open(f'{user.get("id")}.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
              task.get('userId'),
              user.get('username'),
              task.get('completed'),
              task.get('title')])

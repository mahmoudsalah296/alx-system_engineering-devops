#!/usr/bin/python3
"""get data from jsonplaceholder api"""

import requests
import sys


if __name__ == "__main__":
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={'userId': sys.argv[1]}
    )
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )
    json_tasks = tasks.json()
    tasks_number = len(json_tasks)
    complete_tasks = [
        task.get("title") for task in json_tasks if task.get("completed")
    ]
    tasks_completed_num = len(complete_tasks)
    name = user.json().get("name")
    done = f'{tasks_completed_num}/{tasks_number}'
    print(
        f"Employee {name} is done with tasks ({done}):"
    )
    for task in complete_tasks:
        print(f'\t{task}')

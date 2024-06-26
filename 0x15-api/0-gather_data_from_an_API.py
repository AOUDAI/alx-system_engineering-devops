#!/usr/bin/python3
""" Uses a REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":

    Id = int(sys.argv[1])
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{Id}')
    name = r.json().get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': Id})

    tasks = r.json()
    numberOfTasks = len(tasks)
    completedTasks = []
    for task in tasks:
        if task.get('completed'):
            completedTasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        name,
        len(completedTasks),
        numberOfTasks)
        )

    for title in completedTasks:
        print(f"\t {title}")

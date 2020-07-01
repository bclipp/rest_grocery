import pytest  # type: ignore
import requests


def test_manager():
    result = requests.post('http://localhost:5000/manager',
                           data={
                               "username": "bclipp",
                               "password": "12345"
                           })
    print(result.content)


def test_manager_list():
    # localhost:5000/managers/
    pass

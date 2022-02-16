#!/usr/bin/env python3

from time import time
import schemathesis
from fastapi import FastAPI
from schemathesis.checks import not_a_server_error
import requests
import uvicorn
import timeit


# schema = schemathesis.from_path("apiDefinition/swagger.yaml", base_url="http://localhost:8080")

app = FastAPI(openapi_url='/apiDefinition/swagger.yaml')
# app = FastAPI()
schema = schemathesis.from_asgi("/apiDefinition/swagger.yaml", app)


# @schema.parametrize()
# def test_api(case):
#     start = timeit.timeit()
#     response = case.call()
#     end = timeit.timeit()
#     assert (end-start) < 1
#     # case.validate_response(response, checks=(not_a_server_error,))


def test_api():
    querystring = {"authentication":"API_Token"}

    headers = {
        'Content-Type': "application/json",
        'authorization': ""
        }

    response = requests.request("GET", "http://localhost:8080/location", headers=headers, params=querystring)


    # response = requests.get()
    print(response)
    # Raises a validation error
    schema["/location"]["GET"].validate_response(response)
    # Returns a boolean value
    schema["/location"]["GET"].is_response_valid(response)


test_api()


# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='localhost')
#     test_api()

#!/usr/bin/env python3


import yaml

with open(r'apiDefinition/swagger.yaml') as file:
    api_def = yaml.load(file, Loader=yaml.FullLoader)


print(api_def['paths'].keys())

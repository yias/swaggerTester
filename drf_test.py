#!/usr/bin/env python3

from openapi_tester import SchemaTester

# path should be a string
schema_tester = SchemaTester(schema_file_path="apiDefinition/swagger.yaml")




def test_response_documentation(client):
    response = client.get('api/v1/test/1')
    assert response.status_code == 200
    schema_tester.validate_response(response=response)
#!/usr/bin/env python3


from fastapi import FastAPI
import uvicorn




if __name__ == '__main__':
    app = FastAPI(openapi_url='/apiDefinition/swagger.yaml')
    uvicorn.run(app, port=8080, host='localhost')

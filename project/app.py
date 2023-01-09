from fastapi import FastAPI
import importlib

# Dynamic loading of modules
endpoints = importlib.import_module("endpoints")
# Static
# from endpoints import router


app = FastAPI()

app.include_router(endpoints.router)
# app.include_router(router)

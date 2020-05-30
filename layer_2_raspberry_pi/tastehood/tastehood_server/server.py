"""Tastehood server."""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def base():
    return {'hey': 'man'}
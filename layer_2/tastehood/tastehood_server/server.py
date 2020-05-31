"""Tastehood server."""
from fastapi import FastAPI

from tastehood_server.backend import funcs
from tastehood_server.apis.schema import NewTrayInsert

app = FastAPI()


# switch light -
# PUT request
# turn on airconditioner
# turn on humidifier

# insert tray -
# finish germination
# change location
# take tray

# GET
# get humidity -
# tastehood/humidity/2


@app.put('/insert_tray/')
def insert_tray(new_tray: NewTrayInsert):
    funcs.insert_tray(new_tray)

# @app.put('/add_node')
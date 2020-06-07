"""Tastehood server."""
from fastapi import FastAPI

from tastehood_server.backend import funcs
from tastehood_server.apis.schema import (NewTrayInsert, NewShelf, NewNode,
                                          NewSlot, IotStatuses)

app = FastAPI()


# switch light -
# PUT request
# turn on aircondition
# turn on humidifier

# insert tray -
# finish germination
# change location
# take tray

# GET
# get humidity -
# tastehood/humidity/2


@app.put('/insert_tray')
def insert_tray(new_tray: NewTrayInsert):
    funcs.insert_tray(new_tray)


@app.put('/add_node')
def add_node(new_node: NewNode):
    funcs.add_node(new_node)


@app.put('/add_shelf')
def add_shelf(new_shelf: NewShelf):
    print(new_shelf.dict())
    funcs.add_shelf(new_shelf)


@app.put('/add_slot')
def add_slot(new_slot: NewSlot):
    funcs.add_slot(new_slot)


@app.get('/get_iots', response_model=IotStatuses)
def get_iots_status():
    active_iots = funcs.get_active_iots()
    inactice_iots = funcs.get_inactive_iots()
    return IotStatuses(active=active_iots, inactive=inactice_iots)
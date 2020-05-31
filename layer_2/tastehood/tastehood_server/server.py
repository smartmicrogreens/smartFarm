"""Tastehood server."""
from fastapi import FastAPI

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


@app.get('/')
def base():
    return {'hey': 'man'}
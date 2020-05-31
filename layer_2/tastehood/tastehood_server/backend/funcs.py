"""Main backend functionality implementations."""
from tastehood_server.backend.db_interface import get_session
from tastehood_server.apis.schema import NewTrayInsert
from tastehood_server.backend.databases.units import Tray


def insert_tray(tray: NewTrayInsert):
    """Insert a new tray by adding tray to database."""
    with get_session() as sess:
        tray = Tray(**tray.dict())
        sess.add(tray)

"""Main backend functionality implementations."""
from tastehood_server.apis.schema import (NewTrayInsert, NewNode, NewShelf,
                                          NewSlot)
from tastehood_server.backend.databases.units import Tray, Node, Shelf, Slot
from tastehood_server.backend.db_interface import get_session


def insert_tray(tray: NewTrayInsert):
    """Insert a new tray by adding tray to database."""
    with get_session() as sess:
        tray = Tray(**tray.dict())
        sess.add(tray)


def add_node(node: NewNode):
    """Add a new node to the database."""
    with get_session() as sess:
        node = Node(**node.dict())
        sess.add(node)


def add_shelf(shelf: NewShelf):
    """Add a new shelf to the database."""
    with get_session() as sess:
        shelf = Shelf(**shelf.dict())
        sess.add(shelf)


def add_slot(slot: NewSlot):
    """Add a new slot to the database."""
    with get_session() as sess:
        slot = Slot(**slot.dict())
        sess.add(slot)
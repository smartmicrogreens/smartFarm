"""Main backend functionality implementations."""
from typing import List

from tastehood_server.apis.schema import (NewTrayInsert, NewNode, NewShelf,
                                          NewSlot, IotStatuses)
from tastehood_server.backend.databases.units import Tray, Node, Shelf, Slot, ShelfType
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


def get_active_iots() -> List[str]:
    """Get the iots device ids that should be running a routine manager."""
    from sqlalchemy import any_
    with get_session() as sess:
        out = sess.query(Shelf).filter(
            Shelf.shelf_type == ShelfType.growing,
            any_(Slot.n_trays > 0)
        ).all()  # type: List[Shelf]
        return [o.iot_device_id for o in out]


def get_inactive_iots() -> List[str]:
    """Get the iots device ids that should NOT be running a routine manager."""
    from sqlalchemy import all_
    with get_session() as sess:
        out = sess.query(Shelf).filter(
            Shelf.shelf_type == ShelfType.growing,
            all_(Slot.n_trays == 0)
        ).all()  # type: List[Shelf]
        return [o.iot_device_id for o in out]
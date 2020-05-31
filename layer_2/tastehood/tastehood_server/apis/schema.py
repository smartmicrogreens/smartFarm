"""API schemas defined using pydantic."""
from datetime import time
from pydantic import BaseModel

__author__ = 'robin'


class NewTrayInsert(BaseModel):
    """Schema for inserting new trays."""
    id: str
    shelf_id: str
    slot_index: int
    crop_name: str
    initial_tray_weight: float


class NewNode(BaseModel):
    """Add a new node to the system."""
    id: str
    temperature_th: int
    humidity_th: int


class NewShelf(BaseModel):
    """Add a new shelf to the system."""
    id: str
    node_identification_id: str
    sunrise_t: time
    sunset_t: time
    soil_moisture_th: int


class NewSlot(BaseModel):
    """Add a new slot to the system."""
    shelf_id: str
    index: int
    available: bool = True

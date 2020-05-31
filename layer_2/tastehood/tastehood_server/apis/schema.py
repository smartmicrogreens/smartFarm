"""API schemas defined using pydantic."""
from pydantic import BaseModel


class NewTrayInsert(BaseModel):
    """Schema for inserting new trays."""
    id: str
    shelf_id: str
    slot_index: int
    crop_name: str
    initial_tray_weight: float

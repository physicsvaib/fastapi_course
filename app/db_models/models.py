from datetime import datetime
from enum import Enum

from sqlmodel import SQLModel, Field


class ShipmentStatus(str, Enum):
    booked = "booked"
    in_transit = "in_transit"
    delivered = "delivered"
    placed = "placed"


class Shipment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    content: str
    weight: float = Field(le=250)
    destination: int
    estimated_delivery: datetime
    status: ShipmentStatus = Field(default=ShipmentStatus.placed)

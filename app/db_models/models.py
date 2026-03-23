from datetime import datetime, timedelta
from enum import Enum

from sqlmodel import SQLModel, Field


class ShipmentStatus(str, Enum):
    booked = "booked"
    in_transit = "in_transit"
    delivered = "delivered"
    placed = "placed"


def delivery_time():
    return datetime.now() + timedelta(days=3)


class Shipment(SQLModel, table=True):
    __tablename__ = "shipment"

    id: int = Field(primary_key=True, default=None)
    content: str
    weight: float = Field(le=250)
    destination: int
    status: ShipmentStatus = Field(default=ShipmentStatus.placed)

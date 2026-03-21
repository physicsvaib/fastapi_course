from enum import Enum

from pydantic import BaseModel, Field


class ShipmentStatus(str, Enum):
    booked = "booked"
    in_transit = "in_transit"
    delivered = "delivered"
    placed = "placed"


class Shipment(BaseModel):
    content: str = Field(description="What is the content here")
    weight: float = Field(
        lt=250, description="Expected weight here, a bit fuzzy are we"
    )
    status: ShipmentStatus = Field(default=ShipmentStatus.placed)

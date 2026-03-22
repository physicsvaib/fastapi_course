# from enum import Enum

# from pydantic import BaseModel, Field


# class Shipment(BaseModel):
#     content: str = Field(description="What is the content here")
#     weight: float = Field(
#         lt=250, description="Expected weight here, a bit fuzzy are we"
#     )
#     status: ShipmentStatus = Field(default=ShipmentStatus.placed)

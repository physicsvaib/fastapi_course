from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any, List
from .schemas import Shipment, ShipmentStatus
from .db_json import shipment_dict, load_shipments, save_shipments
from .database import Database

gap = FastAPI()

load_shipments()

db = Database("Ship")


@gap.get("/scalar", include_in_schema=False)
def get_scalar_api():
    obj = get_scalar_api_reference(openapi_url=gap.openapi_url)
    return obj


@gap.get("/shipment", response_model=Shipment)
def get_shipment(id: int) -> dict[str, Any]:
    res = db.get_data(id)
    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="What you are looking for is not here",
        )


@gap.post("/shipment")
def post_shipment(data: Shipment) -> dict[str, Any]:
    return db.insert_data(data)


# @gap.get("/shipment/{field}")
# def get_shipment_field(field: str, id: int) -> dict[str, Any]:
#     return {field: shipment_dict[id][field]}


@gap.put("/shipment")
def update_shipment_status(id: int, del_status: ShipmentStatus):
    db.update_data(id, del_status.value)


@gap.delete("/shipment")
def delete_shipment(id: int):
    db.delete_data(id)


# @gap.get("/all_shipments")
# def get_all_shipments() -> dict[str, List[int]]:
#     return {"keys": [i for i in shipment_dict.keys()]}

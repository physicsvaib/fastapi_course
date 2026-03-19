from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any

gap = FastAPI()

shipment_dict = {
    123: {"content": "cargo", "status": "transit", "weight": 20.2},
    124: {"content": "cargo", "status": "placed", "weight": 1.2},
    125: {"content": "cargo", "status": "transit", "weight": 21.52},
    126: {"content": "food", "status": "placed", "weight": 4.2},
    127: {"content": "utils", "status": "done", "weight": 10.2},
}


@gap.get("/scalar", include_in_schema=False)
def get_scalar_api():
    obj = get_scalar_api_reference(
        title="My Custom API Handler", openapi_url=gap.openapi_url
    )
    return obj


@gap.get("/shipment")
def get_shipment(id: int) -> dict[str, str]:
    if id in shipment_dict:
        return {"status": str(shipment_dict[id])}
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Given Id Dont exist can we look again"
        )


@gap.post("/shipment")
def post_shipment(data: dict[str, Any]) -> dict[str, int]:

    if not (data["content"] and data["weight"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="check your inputs"
        )

    content = data["content"]
    weight = data["weight"]

    id = max(shipment_dict.keys()) + 1
    shipment_dict[id] = {"content": content, "status": "placed", "weight": weight}

    return {"id": id}


@gap.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> dict[str, Any]:
    return {field: shipment_dict[id][field]}


@gap.put("/shipment")
def update_shipment_status(id: int, del_status: str):
    if id not in shipment_dict:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="no id found")
    shipment_dict[id]["status"] = del_status
    return shipment_dict[id]


@gap.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    if id in shipment_dict:
        shipment_dict.pop(id)
        return {"detail": f"deleted id {id}"}
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="The thing you are looking for is not here",
        )

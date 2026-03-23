from contextlib import asynccontextmanager
from datetime import datetime, timedelta

from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference

from .db_models.models import Shipment, ShipmentStatus
from .db_models.session import create_db_tables, SessionDep

# from .db_json import shipment_dict, load_shipments, save_shipments
# from .db_models import Database
from .database import Database


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print("Starting App ")
    create_db_tables()
    yield
    print("Stoping App ")


app = FastAPI(lifespan=lifespan_handler)

# load_shipments()

db = Database("Ship")


@app.get("/scalar", include_in_schema=False)
def get_scalar_api():
    obj = get_scalar_api_reference(openapi_url=app.openapi_url)
    return obj


@app.get("/shipment", response_model=Shipment)
def get_shipment(id: int, session: SessionDep):
    res = session.get(Shipment, id)

    if res is not None:
        return res
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="What you are looking for is not here",
        )


@app.post("/shipment")
def post_shipment(data: Shipment, session: SessionDep) -> dict[str, int]:
    new_shipment = Shipment(
        **data.model_dump(),
    )
    session.add(new_shipment)
    session.commit()

    session.refresh(new_shipment)
    return {"id": new_shipment.id}


# @gap.get("/shipment/{field}")
# def get_shipment_field(field: str, id: int) -> dict[str, Any]:
#     return {field: shipment_dict[id][field]}


@app.put("/shipment")
def update_shipment_status(id: int, del_status: ShipmentStatus, session: SessionDep):
    ship = session.get(Shipment, id)
    ship.status = del_status

    session.add(ship)
    session.commit()
    session.refresh(ship)

    return ship


@app.delete("/shipment")
def delete_shipment(id: int, session: SessionDep):
    session.delete(session.get(Shipment, id))
    session.commit()


# @gap.get("/all_shipments")
# def get_all_shipments() -> dict[str, List[int]]:
#     return {"keys": [i for i in shipment_dict.keys()]}

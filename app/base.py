from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

gap = FastAPI()


@gap.get("/scalar")
def get_scalar_api():
    obj = get_scalar_api_reference(
        title="My Custom API Handler", openapi_url=gap.openapi_url
    )
    return obj


@gap.get("/hey")
def get_hey():
    return {"hey": "there"}

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

gap = FastAPI()

dic = {123: "Pass", 213: "Transit", 321: "Fail"}


@gap.get("/scalar")
def get_scalar_api():
    obj = get_scalar_api_reference(
        title="My Custom API Handler", openapi_url=gap.openapi_url
    )
    return obj


@gap.get("/hey/{id}")
def get_hey(id: int) -> dict[str, str]:
    return {"hey": f"there, {dic[id] if id in dic else f'nothing found with {id}'}"}

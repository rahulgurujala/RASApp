from pydantic import BaseModel
from starlette.status import HTTP_200_OK


class ResponseSchema(BaseModel):
    payload: dict
    status_code: int = HTTP_200_OK
    error_code: int = 0

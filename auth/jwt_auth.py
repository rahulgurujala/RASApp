import jwt
from fastapi import Header, HTTPException

from settings import SECRET_KEY


def get_current_user(
    authorization: str = Header(None),
):
    try:
        token = authorization.split(" ")[1]
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Invalid authentication credentials"
        ) from e

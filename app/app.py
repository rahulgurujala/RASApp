import jwt
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from werkzeug.security import check_password_hash

from auth.jwt import get_current_user
from db.models import User
from schema.response import ResponseSchema
from schema.users import UserRegisterSchema, LogIn
from settings import session, SECRET_KEY

app = FastAPI(title="RAS")


@app.get("/", response_model=ResponseSchema, status_code=HTTP_200_OK)
def test():
    return ResponseSchema({"message": "everything working fine"})


@app.post("/register", response_model=ResponseSchema, status_code=HTTP_200_OK)
def register(user: UserRegisterSchema, session: Session = Depends(session)):
    user_data = user.dict()

    if User.get(session=session, username=user_data.get("username")):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="user already in exists"
        )

    user = User(**user_data)
    user.create(session, user)
    return ResponseSchema(payload={"message": "User created successfully"})


@app.post("/login", response_model=ResponseSchema, status_code=HTTP_200_OK)
def login(user: LogIn, session: Session = Depends(session)):
    user = User.get(session=session, username=user.username)

    if not user or check_password_hash(user.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = jwt.encode({"sub": user.id}, SECRET_KEY, algorithm="HS256")
    return ResponseSchema(payload={"access_token": token})


@app.get("/home", response_model=ResponseSchema, status_code=HTTP_200_OK)
def home(session: Session = Depends(session), current_user=Depends(get_current_user)):
    return ResponseSchema(
        payload={
            "data": User.get_all(session=session),
            "current_user": current_user,
        }
    )

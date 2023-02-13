from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK
from werkzeug.security import generate_password_hash
from schema.users import UserRegisterSchema

from settings import session

app = FastAPI(title="RAS")


@app.get("/")
def home(session: Session = Depends(session)):
    return {"message": "everything working fine"}

@app.post('/register')
def register(
        user_register_schema: UserRegisterSchema,
        session: Session = Depends(session)
    ):
    return {'message': user_register_schema.date_of_birth}
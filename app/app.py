import jwt
from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from werkzeug.security import check_password_hash

from auth.jwt_auth import get_current_user
from db.models import Image, User
from schema.image import ImageSchema
from schema.response import ResponseSchema
from schema.users import LogIn, UserRegisterSchema
from settings import SECRET_KEY, session
from utils.store_img import generate_presigned_url, save_image_file

app = FastAPI(title="RAS")


@app.get("/", response_model=ResponseSchema, status_code=HTTP_200_OK)
def test():
    return ResponseSchema(payload={"message": "everything working fine"})


@app.post("/register", response_model=ResponseSchema, status_code=HTTP_200_OK)
def register(user: UserRegisterSchema, session: Session = Depends(session)):
    user_data = user.dict()

    if User.get_by(session=session, username=user_data.get("username")):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="user already in exists"
        )

    user = User.create(session, **user_data)
    return ResponseSchema(
        payload={"message": f"User {user.username} created successfully"}
    )


@app.post("/login", response_model=ResponseSchema, status_code=HTTP_200_OK)
def login(login_user: LogIn, session: Session = Depends(session)):
    user = User.get_by(session=session, username=login_user.username)

    if not user or not check_password_hash(user.password, login_user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    token = jwt.encode({"sub": user.id}, SECRET_KEY, algorithm="HS256")
    return ResponseSchema(payload={"access_token": token})


# TODO: Need to Refactor
@app.get("/home", response_model=ResponseSchema, status_code=HTTP_200_OK)
def home(session: Session = Depends(session), current_user=Depends(get_current_user)):
    user = User.get_by_id(session=session, _id=current_user["sub"])
    images = []
    for i in Image.filter_by(session=session, user_id=user.id):
        i.image_url = generate_presigned_url(i.image_url)
        images.append(i)
    return ResponseSchema(payload={"images": images})


@app.post("/uploadfile", response_model=ResponseSchema, status_code=HTTP_200_OK)
def create_upload_file(
    text: str = Form(...),
    file: UploadFile = File(...),
    session: Session = Depends(session),
    current_user=Depends(get_current_user),
):
    image_path = save_image_file(file)
    ImageSchema(user_id=current_user.get("sub"), text=text, image_path=image_path)
    image = Image(
        user_id=current_user.get("sub"),
        image_url=image_path,
        text=text,
    )
    image = image.create(session=session, obj=image)
    return ResponseSchema(payload={"filename": image.image_url, "image_id": image.id})

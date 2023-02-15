from pydantic import BaseModel


class ImageSchema(BaseModel):
    user_id: int
    text: str
    image_path: str

from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: str
    name: str
    email: str
    phone_number: str
    birthdate: datetime
    gender: str
    ethnicity: str
    created_at: datetime
    updated_at: datetime

class UserList(BaseModel):
    users: list[UserSchema]
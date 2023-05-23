from pydantic import BaseModel

"""
We use `pydantic` as our serializer,
We can use this models in both database, Json raw data.

"""

class userSchema(BaseModel):
    username: str
    email: str
    full_name: str
    active: bool

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
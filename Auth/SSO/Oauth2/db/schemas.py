from pydantic import BaseModel

"""
We use `pydantic` as our serializer,
We can use this models in both database, Json raw data.

"""

class userSchema(BaseModel):
    username: str
    full_name: str
    active: bool

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None


class UserInDB(userSchema):
    password: str


def test_user_schema():
    user = UserInDB(
        username="parsa",
        full_name="parsa riyahi",
        active=True,
        password="parsa1234",
    )

    print(*user.dict().values())

test_user_schema()
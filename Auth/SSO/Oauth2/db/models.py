from sqlalchemy import String, Boolean, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    full_name: Mapped[str] = mapped_column(String(30))
    active: Mapped[bool] = mapped_column(Boolean())
    password: Mapped[str] = mapped_column(String(30))


engine = create_engine("sqlite:///Auth/SSO/Oauth2/db/database.db", echo=True)
Base.metadata.create_all(engine)

def insert_fake_data():
    with Session(engine) as session :
        user1 = User(
            username="parsa",
            full_name="parsa riyahi",
            active=True,
            password="parsa1234"
        )

        session.add(user1)
        session.commit()

def select_fake_data() :
    with Session(engine) as session:
        query = select(User).where(User.username.in_(["parsa"]))

        for user in session.scalars(query):
            print(user.id)

insert_fake_data()
select_fake_data()
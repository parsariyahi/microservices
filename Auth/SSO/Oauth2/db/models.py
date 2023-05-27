from sqlalchemy import String, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    full_name: Mapped[str] = mapped_column(String(30))
    active: Mapped[bool] = mapped_column(Boolean())
    password: Mapped[str] = mapped_column(String(30))

engine = create_engine("sqlite:///./some.db", echo=True)


Base.metadata.create_all(engine)
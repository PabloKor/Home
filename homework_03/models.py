"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func
)

from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), unique=True)
    email = Column(String(32), nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=func.now())

    posts = relationship('Post', back_populates='user')
    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, " \
               f"name={self.name!r}, " \
               f"username={self.username!r}, " \
               f"email={self.email!r}, " \
               f"create_date={self.create_date!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, title={self.title!r}, body = {self.body!r}, user_id={self.user_id!r}"

    def __repr__(self):
        return str(self)

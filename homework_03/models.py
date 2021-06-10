"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from datetime import datetime
from typing import List

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def save_users_data_in_db(u_data: List[dict]):
    async with Session() as session:
        async with session.begin():
            for user_data in u_data:
                user = User(name=user_data['name'], username=user_data['username'], email=user_data['email'])
                session.add(user)
            # после выхода из контекста  async with session.begin(): коммит делается автоматически


async def save_posts_data_in_db(p_data: List[dict]):
    async with Session() as session:
        async with session.begin():
            for post_data in p_data:
                post = Post(title=post_data['title'], body=post_data['body'], user_id=post_data['userId'])
                session.add(post)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    username = Column(String(32), nullable=False)
    email = Column(String(32), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    posts = relationship('Post', back_populates='user')

    # __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name = {self.name!r}, username = {self.username!r},' \
               f' email={self.email},' \
               f' created_at={self.created_at!r})'

    def __repr__(self):
        return str(self)


# relation many(Post)  to one(User)  (Post.user)
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')

    # __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, body = {self.body!r}"

    def __repr__(self):
        return str(self)
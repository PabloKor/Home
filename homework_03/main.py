"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from typing import List
from homework_03.jsonplaceholder_requests import fetch_json, POSTS_DATA_URL, USERS_DATA_URL
from homework_03.models import Base, engine, Session, User, Post
import asyncio


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def users_data_in_db(u_data: List[dict]):
    async with Session() as session:
        async with session.begin():
            for user_data in u_data:
                user = User(name=user_data['name'], username=user_data['username'], email=user_data['email'])
                session.add(user)



async def posts_data_in_db(p_data: List[dict]):
    async with Session() as session:
        async with session.begin():
            for post_data in p_data:
                post = Post(title=post_data['title'], body=post_data['body'], user_id=post_data['userId'])
                session.add(post)


async def async_main():
    await create_table()
    users_data, posts_data = await asyncio.gather(fetch_json(USERS_DATA_URL),
                                                  fetch_json(POSTS_DATA_URL))
    await users_data_in_db(users_data)
    await posts_data_in_db(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

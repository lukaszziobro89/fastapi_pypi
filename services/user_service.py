from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from sqlalchemy import select, func

from data import db_session
from data.user import User


async def user_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(User.id))
        result = await session.execute(query)
        return result.scalar()


def create_account(name: str, email: str, password: str) -> User:
    session = db_session.create_session()

    try:
        user = User()
        user.email = email
        user.name = name
        user.hash_password = crypto.hash(password, rounds=172_434)

        session.add(user)
        session.commit()

        return user
    finally:
        session.close()


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return user

        if not crypto.verify(password, user.hash_password):
            return None

        return user
    finally:
        session.close()


def get_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()

    try:
        return session.query(User).filter(User.id == user_id).first()
    finally:
        session.close()


def get_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        return session.query(User).filter(User.email == email).first()
    finally:
        session.close()

from sqlalchemy import Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///English.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] =  mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(125))
    achievements_past: Mapped[str] = mapped_column(String(125))
    achievements_present: Mapped[str] = mapped_column(String(125))
    achievements_future: Mapped[str] = mapped_column(String(125))
    complete_tests: Mapped[int] = mapped_column(Integer)


class Admin(Base):
    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, nullable=True)


class TestPast(Base):
    __tablename__ = 'testsPast'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.tg_id'))
    test_past_1: Mapped[int] = mapped_column()
    test_past_2: Mapped[int] = mapped_column()
    test_past_3: Mapped[int] = mapped_column()
    test_past_4: Mapped[int] = mapped_column()


class TestPresent(Base):
    __tablename__ = 'testsPresent'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.tg_id'))
    test_present_1: Mapped[int] = mapped_column()
    test_present_2: Mapped[int] = mapped_column()
    test_present_3: Mapped[int] = mapped_column()
    test_present_4: Mapped[int] = mapped_column()


class TestFuture(Base):
    __tablename__ = 'testsFuture'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.tg_id'))
    test_future_1: Mapped[int] = mapped_column()
    test_future_2: Mapped[int] = mapped_column()
    test_future_3: Mapped[int] = mapped_column()
    test_future_4: Mapped[int] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



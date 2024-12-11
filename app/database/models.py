from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///English.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id =  mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(125))

class Test(Base):
    __tablename__ = 'tests'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    test_past: Mapped[str] = mapped_column(String(125))
    test_present: Mapped[str] = mapped_column(String(125))
    test_future: Mapped[str] = mapped_column(String(125))
    test_past_1: Mapped[int] = mapped_column()
    test_past_2: Mapped[int] = mapped_column()
    test_past_3: Mapped[int] = mapped_column()
    test_past_4: Mapped[int] = mapped_column()
    test_present_1: Mapped[int] = mapped_column()
    test_present_2: Mapped[int] = mapped_column()
    test_present_3: Mapped[int] = mapped_column()
    test_present_4: Mapped[int] = mapped_column()
    test_future_1: Mapped[int] = mapped_column()
    test_future_2: Mapped[int] = mapped_column()
    test_future_3: Mapped[int] = mapped_column()
    test_future_4: Mapped[int] = mapped_column()



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



from core.config import get_app_settings
from core.settings.app import AppSettings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


settings = get_app_settings()

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/asyncalchemy"

engine = create_async_engine(settings.database_url, pool_size=20, max_overflow=0, echo=True)
async_session = AsyncSession(engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

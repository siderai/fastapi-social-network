from sqlalchemy.ext.asyncio import AsyncSession


# Как передать сессию?
class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @property
    def get_session(self) -> AsyncSession:
        return self._session

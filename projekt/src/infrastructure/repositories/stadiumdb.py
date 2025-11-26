"""Module containing stadium database repository implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.domain.stadium import Stadium, StadiumIn
from src.core.repositories.istadium import IStadiumRepository
from src.db import stadium_table, database


class StadiumRepository(IStadiumRepository):
    """A class implementing the stadium repository."""

    async def get_stadium_by_id(self, stadiumsId: int) -> Any | None:
        """The method getting a stadium from the data storage.

        Args:
            stadiumsID (int): The id of the stadium.

        Returns:
            Any | None: The stadium data if exists.
        """

        stadium = await self._get_by_id(stadiumsId)

        return Stadium(**dict(stadium)) if stadium else None

    async def get_all_stadiums(self) -> Iterable[Any]:
        """The method getting all stadiums from the data storage.

        Returns:
            Iterable[Any]: The collection of the all stadiums.
        """

        query = stadium_table.select().order_by(stadium_table.c.name.asc())
        stadiums = await database.fetch_all(query)

        return [Stadium(**dict(stadium)) for stadium in stadiums]

    async def add_stadium(self, data: StadiumIn) -> Any | None:
        """The method adding new stadium to the data storage.

        Args:
            data (StadiumIn): The attributes of the stadium.

        Returns:
            Any | None: The newly created stadium.
        """

        query = stadium_table.insert().values(**data.model_dump())
        new_stadium_id = await database.execute(query)
        new_stadium = await self._get_by_id(new_stadium_id)

        return Stadium(**dict(new_stadium)) if new_stadium else None

    async def update_stadium(
        self,
        stadiumsId: int,
        data: StadiumIn,
    ) -> Any | None:
        """The method updating stadium data in the data storage.

        Args:
            stadium_id (int): The stadium id.
            data (StadiumIn): The attributes of the stadium.

        Returns:
            Any | None: The updated stadium.
        """

        if self._get_by_id(stadiumsId):
            query = (
                stadium_table.update()
                .where(stadium_table.c.id == stadiumsId)
                .values(**data.model_dump())
            )
            await database.execute(query)

            stadium = await self._get_by_id(stadiumsId)

            return Stadium(**dict(stadium)) if stadium else None

        return None

    async def delete_stadium(self, stadiumsId: int) -> bool:
        """The method updating removing stadium from the data storage.

        Args:
            stadiumsId (int): The stadium id.

        Returns:
            bool: Success of the operation.
        """

        if self._get_by_id(stadiumsId):
            query = stadium_table \
                .delete() \
                .where(stadium_table.c.id == stadiumsId)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, stadiumsId: int) -> Record | None:
        """A private method getting stadium from the DB based on its ID.

        Args:
            stadiumsId (int): The ID of the stadium.

        Returns:
            Any | None: Stadium record if exists.
        """

        query = (
            stadium_table.select()
            .where(stadium_table.c.id == stadiumsId)
            .order_by(stadium_table.c.name.asc())
        )

        return await database.fetch_one(query)
"""Module containing club repository database implementation."""

from typing import Any, Iterable

from asyncpg import Record  # type: ignore

from src.core.domain.club import Club, ClubIn
from src.core.repositories.iclub import IClubRepository
from src.db import club_table, database


class ClubRepository(IClubRepository):
    """A class implementing the database club repository."""

    async def get_club_by_id(self, clubId: int) -> Any | None:
        """The method getting a club from the temporary data storage.

        Args:
            clubId (int): The id of the club.

        Returns:
            Any | None: The club data if exists.
        """

        club = await self._get_by_id(clubId)

        return Club(**dict(club)) if club else None

    async def get_all_clubs(self) -> Iterable[Any]:
        """The abstract getting all clubs from the data storage.

        Returns:
            Iterable[Any]: The collection of the all clubs.
        """

        query = club_table.select().order_by(club_table.c.name.asc())
        clubs = await database.fetch_all(query)

        return [Club(**dict(club)) for club in clubs]



    async def add_club(self, data: ClubIn) -> Any | None:
        """The abstract adding new club to the data storage.

        Args:
            data (ClubIn): The attributes of the club.

        Returns:
            Any | None: The newly created club.
        """

        query = club_table.insert().values(**data.model_dump())
        new_club_id = await database.execute(query)
        new_club = await self._get_by_id(new_club_id)

        return Club(**dict(new_club)) if new_club else None

    async def update_club(
            self,
            clubId: int,
            data: ClubIn,
    ) -> Any | None:
        """The abstract updating club data in the data storage.

        Args:
            clubId (int): The club id.
            data (ClubIn): The attributes of the club.

        Returns:
            Any | None: The updated club.
        """

        if self._get_by_id(clubId):
            query = (
                club_table.update()
                .where(club_table.c.id == clubId)
                .values(**data.model_dump())
            )
            await database.execute(query)

            club = await self._get_by_id(clubId)

            return Club(**dict(club)) if club else None

        return None

    async def delete_club(self, clubId: int) -> bool:
        """The abstract updating removing club from the data storage.

        Args:
            clubId (int): The club id.
        """

        if self._get_by_id(clubId):
            query = club_table \
                .delete() \
                .where(club_table.c.id == clubId)
            await database.execute(query)

            return True

        return False

    async def _get_by_id(self, clubId: int) -> Record | None:
        """A private method getting club from the DB based on its ID.

        Args:
            clubId (int): The ID of the club.

        Returns:
            Any | None: Club record if exists.
        """

        query = (
            club_table.select()
            .where(club_table.c.id == clubId)
            .order_by(club_table.c.name.asc())
        )

        return await database.fetch_one(query)
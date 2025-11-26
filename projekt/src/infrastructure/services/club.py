"""Module containing country service implementation."""

from typing import Iterable

from src.core.domain.club import Club, ClubIn
from src.core.repositories.iclub import IClubRepository
from src.infrastructure.services.iclub import IClubService


class ClubService(IClubService):
    """A class implementing the club service."""

    _repository: IClubRepository

    def __init__(self, repository: IClubRepository) -> None:
        """The initializer of the `club service`.

        Args:
            repository (IClubRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_club_by_id(self, clubId: int) -> Club | None:
        """The abstract getting a club from the repository.

        Args:
            clubId (int): The id of the club.

        Returns:
            Club | None: The club data if exists.
        """

        return await self._repository.get_club_by_id(clubId)

    async def get_all_countries(self) -> Iterable[Club]:
        """The abstract getting all clubs from the repository.

        Returns:
            Iterable[Club]: The collection of the all club.
        """

        return await self._repository.get_all_clubs()

    async def get_countries_by_stadium(
            self,
            StadiumId: int,
    ) -> Iterable[Club]:
        """The abstract getting all provided stadium's club
            from the repository.

        Args:
            stadiumId (int): The id of the stadium.

        Returns:
            Iterable[Stadium]: The collection of the countries.
        """

        return await self._repository.get_countries_by_stadium(StadiumId)

    async def add_country(self, data: ClubIn) -> Club | None:
        """The abstract adding new club to the repository.

        Args:
            data (ClubIn): The attributes of the club.

        Returns:
            Club | None: The newly created club.
        """

        return await self._repository.add_club(data)

    async def update_club(
            self,
            clubId: int,
            data: ClubIn,
    ) -> Club | None:
        """The abstract updating club data in the repository.

        Args:
            clubId (int): The club id.
            data (ClubIn): The attributes of the club.

        Returns:
            Club | None: The updated club.
        """

        return await self._repository.update_club(
            clubId=clubId,
            data=data,
        )

    async def delete_country(self, clubId: int) -> bool:
        """The abstract updating removing club from the repository.

        Args:
            clubId (int): The club id.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_club(clubId)

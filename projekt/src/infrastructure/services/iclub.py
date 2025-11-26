"""Module containing country service abstractions."""

from abc import ABC, abstractmethod

from typing import Iterable

from src.core.domain.club import Club, ClubIn


class IClubService(ABC):
    """An abstract class representing protocol of club repository."""

    @abstractmethod
    async def get_club_by_id(self, clubId: int) -> Club | None:
        """The abstract getting a club from the repository.

        Args:
            clubId (int): The id of the club.

        Returns:
            Club | None: The club data if exists.
        """

    @abstractmethod
    async def get_all_clubs(self) -> Iterable[Club]:
        """The abstract getting all clubs from the repository.

        Returns:
            Iterable[Club]: The collection of the all clubs.
        """

    @abstractmethod
    async def get_club_by_place(
            self,
            place: str,
    ) -> Iterable[Club]:
        """The abstract getting all provided clubs


        Returns:
            Iterable[Club]: The collection of the clubs.
        """

    @abstractmethod
    async def add_club(self, data: ClubIn) -> Club | None:
        """The abstract adding new club to the repository.

        Args:
            data (CountryIn): The attributes of the club.

        Returns:
            Club | None: The newly created club.
        """

    @abstractmethod
    async def update_club(
            self,
            clubId: int,
            data: ClubIn,
    ) -> Club | None:
        """The abstract updating club data in the repository.

        Args:
            clubId (int): The country id.
            data (ClubIn): The attributes of the country.

        Returns:
            Country | None: The updated country.
        """

    @abstractmethod
    async def delete_club(self, clubId: int) -> bool:
        """The abstract updating removing club from the repository.

        Args:
            clubId (int): The club id.

        Returns:
            bool: Success of the operation.
        """

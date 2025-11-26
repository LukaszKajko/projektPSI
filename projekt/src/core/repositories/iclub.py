"""Module containing contient repository abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.club import Club, ClubIn


class IClubRepository(ABC):
    """An abstract class representing protocol of continent repository."""

    @abstractmethod
    async def get_continent_by_id(self, club_id: int) -> Club | None:
        """The abstract getting a club from the data storage.

        Args:
            club_id (int): The id of the club.

        Returns:
            club | None: The club data if exists.
        """

    @abstractmethod
    async def get_all_clubs(self) -> Iterable[Club]:
        """The abstract getting all clus from the data storage.

        Returns:
            Iterable[Club]: The collection of the all continents.
        """

    @abstractmethod
    async def add_club(self, data: ClubIn) -> None:
        """The abstract adding new club to the data storage.

        Args:
            data (ClubIn): The attributes of the club.
        """

    @abstractmethod
    async def update_club(
        self,
        club_id: int,
        data: ClubIn,
    ) -> Club | None:
        """The abstract updating club data in the data storage.

        Args:
            club_id (int): The continent id.
            data (ClubIn): The attributes of the club.

        Returns:
            Club | None: The updated club.
        """

    @abstractmethod
    async def delete_club(self, club_id: int) -> bool:
        """The abstract updating removing club from the data storage.

        Args:
            club_id (int): The club id.

        Returns:
            bool: Success of the operation.
        """
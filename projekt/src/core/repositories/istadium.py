from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.stadium import Stadium, StadiumIn


class IStadiumRepository(ABC):
    """An abstract class representing protocol of stadiums repository."""

    @abstractmethod
    async def get_all_stadiums(self) -> Iterable[Stadium]:
        """The abstract getting all stadiums from the data storage.

        Returns:
            Iterable[Stadium]: Stadiums in the data storage.
        """

    @abstractmethod
    async def get_by_id(self, stadiumId: int) -> Stadium | None:
        """The abstract getting stadium by provided id.

        Args:
            stadium_id (int): The id of the airport.

        Returns:
            Stadium | None: The stadium details.
        """

        @abstractmethod
        async def get_by_stadiumName(self, stadiumsName: str) -> Stadium | None:
            """The abstract getting stadium by provided name.

            Args:
                stadiumsName (str): The name of the airport.

            Returns:
                Stadium | None: The stadium details.
            """

        @abstractmethod
        async def get_by_clubName(self, clubName: str) -> Stadium | None:
            """The abstract getting stadium by provided club's name.

            Args:
                clubName (istr): The name of the club.

            Returns:
                clubName | None: The stadium details.
            """

        @abstractmethod
        async def get_by_user(self, user_id: int) -> Iterable[Stadium]:
            """The abstract getting stadiums by user who added them.

            Args:
                user_id (int): The id of the user.

            Returns:
                Iterable[Stadium]: The stadium collection.
            """

        @abstractmethod
        async def add_stadium(self, data: StadiumIn) -> None:
            """The abstract adding new stadium to the data storage.

            Args:
                data (StadiumIn): The details of the new stadium.
            """

        @abstractmethod
        async def update_stadium(
                self,
                airport_id: int,
                data: StadiumIn,
        ) -> Stadium | None:
            """The abstract updating stadium data in the data storage.

            Args:
                stadium_id (int): The id of the stadium.
                data (StadiumIn): The details of the updated stadium.

            Returns:
                Stadium | None: The updated stadium details.
            """

        @abstractmethod
        async def delete_airport(self, stadium_id: int) -> bool:
            """The abstract updating removing stadium from the data storage.

            Args:
                stadium_id (int): The id of the stadium.

            Returns:
                bool: Success of the operation.
            """


"""Module containing airport service abstractions."""

from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.stadium import Stadium, StadiumBroker
from src.infrastructure.dto.stadiumdto import StadiumDTO


class IStadiumService(ABC):
    """A class representing stadium repository."""

    @abstractmethod
    async def get_all(self) -> Iterable[StadiumDTO]:
        """The method getting all stadiums from the repository.

        Returns:
            Iterable[StadiumDTO]: All stadiums.
        """

    @abstractmethod
    async def get_by_clubName(self, stadiumsId: int) -> Iterable[Stadium]:
        """The method getting stadiums assigned to particular id.

               Args:
                   stadiumsId (int): The id of the stadium.

               Returns:
                   Iterable[Stadium]: Stadiums assigned to an id.
               """


    @abstractmethod
    async def get_by_stadiumName(self, amountOfSeats: int) -> Iterable[Stadium]:
        """The method getting stadiums assigned to particular amountOfSeats.

                       Args:
                           stadiumsId (int): The amount of seats of the stadium.

                       Returns:
                           Iterable[Stadium]: Stadiums assigned.
                       """



    @abstractmethod
    async def get_by_clubName(self, clubName: str) -> StadiumDTO | None:
        """The method getting airport by provided clubName code.

               Args:
                   clubName (str): The clubName  of the stadium.

               Returns:
                   StadiumDTO | None: The stadium details.
               """


    @abstractmethod
    async def get_by_stadiumName(self, stadiumName: str) -> StadiumDTO | None:
        """The method getting stadium by provided name.

               Args:
                    StadiumName (str): The name of the stadium.

               Returns:
                   StadiumDTO | None: The stadium details.
               """




    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Stadium]:
        """The method getting stadiums by user who added them."""



    @abstractmethod
    async def add_stadium(self, data: StadiumBroker) -> Stadium | None:
        """The method adding new stadium to the data storage.

        Args:
            data (StadiumBroker): The details of the new stadium.

        Returns:
            Stadium | None: Full details of the newly added airport.
        """

    @abstractmethod
    async def update_stadium(
        self,
        stadiumsId: int,
        data: StadiumBroker,
    ) -> Stadium | None:
        """The method updating stadium data in the data storage.

        Args:
            stadiumID (int): The id of the stadium.
            data (StadiumBroker): The details of the updated stadium.

        Returns:
            Stadium | None: The updated stadium details.
        """

    @abstractmethod
    async def delete_stadium(self, stadiumId: int) -> bool:
        """The method updating removing stadium from the data storage.

        Args:
            stadiumId (int): The id of the airport.

        Returns:
            bool: Success of the operation.
        """
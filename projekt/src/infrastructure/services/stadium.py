"""Module containing continent service implementation."""

from typing import Iterable

from src.core.domain.stadium import Stadium, StadiumBroker
from src.core.repositories.istadium import IStadiumRepository
from src.infrastructure.dto.stadiumdto import StadiumDTO
from src.infrastructure.services.istadium import IStadiumService


class StadiumService(IStadiumService):
    """A class implementing the airport service."""

    _repository: IStadiumRepository

    def __init__(self, repository: IStadiumRepository) -> None:
        """The initializer of the `airport service`.

        Args:
            repository (IStadiumRepository): The reference to the repository.
        """

        self._repository = repository

    async def get_all(self) -> Iterable[StadiumDTO]:
        """The method getting all stadiums from the repository.

        Returns:
            Iterable[StadiumDTO]: All stadiums.
        """

        return await self._repository.get_all_stadiums()

    async def get_by_amountOfSeats(self, amountOfSeats: int) -> Iterable[Stadium]:
        """The method getting stadiums assigned to particular amount of seats.

            Iterable[Stadium]: Stadium assigned to seats.
        """

        return await self._repository.get_by_amountOfSeats(amountOfSeats)

    async def get_by_id(self, stadiumId: int) -> StadiumDTO | None:
        """The method getting stadium by provided id.

        Args:
            stadiumId (int): The id of the stadium.

        Returns:
            StadiumDTO | None: The stadium details.
        """

        return await self._repository.get_by_id(stadiumId)

    async def get_by_clubName(self, clubName: str) -> StadiumDTO | None:
        """The method getting stadium by provided name of club.

        Args:
            clubName (str): The name of stadium's clib.

        Returns:
            StadiumDTO | None: The stadium details.
        """

        return await self._repository.get_by_clubName(clubName)

    async def get_by_iata(self, stadiumName: str) -> StadiumDTO | None:
        """The method getting stadiumairport by provided name.

        Args:
            stadiumName (str): The name of stadium.

        Returns:
            StadiumDTO | None: The stadium details.
        """

        return await self._repository.get_by_stadiumName(stadiumName)

    async def get_by_user(self, user_id: int) -> Iterable[Stadium]:
        """The method getting airports by user who added them.

        Args:
            user_id (int): The id of the user.

        Returns:
            Iterable[Airport]: The airport collection.
        """

        return await self._repository.get_by_user(user_id)

    async def add_airport(self, data: StadiumBroker) -> Stadium | None:
        """The method adding new airport to the data storage.

        Args:
            data (AirportBroker): The details of the new airport.

        Returns:
            Airport | None: Full details of the newly added airport.
        """

        return await self._repository.add_stadium(data)

    async def update_stadium(
            self,
            airport_id: int,
            data: StadiumBroker,
    ) -> Stadium | None:
        """The method updating airport data in the data storage.

        Args:
            airport_id (int): The id of the airport.
            data (AirportBroker): The details of the updated airport.

        Returns:
            Airport | None: The updated airport details.
        """

        return await self._repository.update_stadium(
            stadiumsId=stadiumsId,
            data=data,
        )

    async def delete_airport(self, stadiumsId: int) -> bool:
        """The method updating removing airport from the data storage.

        Args:
            airport_id (int): The id of the airport.

        Returns:
            bool: Success of the operation.
        """

        return await self._repository.delete_stadiums(stadiumsId)

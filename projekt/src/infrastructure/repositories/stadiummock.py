"""Module containing stadium repository implementation."""

from typing import Iterable

from src.core.repositories.istadium import IStadiumRepository
from src.core.domain.stadium import Stadium, StadiumIn
from src.infrastructure.repositories.db import stadiums


class StadiumMockRepository(IStadiumRepository):
    """A class representing stadium repository."""

    async def get_all_stadiums(self) -> Iterable[Stadium]:
        """The method getting all stadiums from the data storage.

        Returns:
            Iterable[Stadium]: Stadiums in the data storage.
        """

        return stadiums

    async def get_by_club(self, club_id: int) -> Iterable[Stadium]:
        """The method getting airports assigned to particular club.

        Args:
            club_id (int): The id of the country.

        Returns:
            Iterable[Club]: Stadiums assigned to a club.
        """

        return list(filter(lambda x: x.country_id == club_id, stadiums))

    async def get_by_continent(self, stadiumsName: str) -> Iterable[Stadium]:
        """The method getting stadiums assigned to particular continent.

        Args:
            stadiumsName (str): The name of stadium.

        Returns:
            Iterable[Stadium]: Stadium assigned to a name.
        """

        return stadiums

    async def get_by_id(self, stadiumId: int) -> Stadium | None:
        """The method getting stadium by provided id.

        Args:
            stadium_id (int): The id of the stadium.

        Returns:
            Airport | None: The airport details.
        """

        return next((obj for obj in airports if obj.id == airport_id), None)

    async def get_by_icao(self, icao_code: str) -> Airport | None:
        """The method getting airport by provided ICAO code.

        Args:
            icao_code (str): The ICAO code of the airport.

        Returns:
            Airport | None: The airport details.
        """

        return next(
            (obj for obj in airports if obj.icao_code == icao_code),
            None,
        )

    async def get_by_iata(self, iata_code: str) -> Airport | None:
        """The method getting airport by provided IATA code.

        Args:
            icao_code (str): The IATA code of the airport.

        Returns:
            Airport | None: The airport details.
        """

        return next(
            (obj for obj in airports if obj.iata_code == iata_code),
            None,
        )

    async def get_by_user(self, user_id: int) -> Iterable[Airport]:
        """The method getting airports by user who added them.

        Args:
            user_id (int): The id of the user.

        Returns:
            Iterable[Airport]: The airport collection.
        """

        return list(filter(lambda x: x.user_id == user_id, airports))

    async def get_by_location(
            self,
            latitude: float,
            longitude: float,
            radius: float,
    ) -> Iterable[Airport]:
        """The method getting airports by raduis of the provided location.

        Args:
            latitude (float): The geographical latitude.
            longitude (float): The geographical longitude.
            radius (float): The radius airports to search.

        Returns:
            Iterable[Airport]: The result airport collection.
        """

        return airports

    async def add_airport(self, data: AirportIn) -> None:
        """The method adding new airport to the data storage.

        Args:
            data (AirportIn): The details of the new airport.

        Returns:
            Airport: Full details of the newly added airport.
        """

        airports.append(data)

    async def update_airport(
            self,
            airport_id: int,
            data: AirportIn,
    ) -> Airport | None:
        """The method updating airport data in the data storage.

        Args:
            airport_id (int): The id of the airport.
            data (AirportIn): The details of the updated airport.

        Returns:
            Airport | None: The updated airport details.
        """

        if airport_pos := \
                next(filter(lambda x: x.id == airport_id, airports)):
            airports[airport_pos] = data

            return Airport(id=0, **data.model_dump())

        return None

    async def delete_airport(self, airport_id: int) -> bool:
        """The method updating removing airport from the data storage.

        Args:
            airport_id (int): The id of the airport.

        Returns:
            bool: Success of the operation.
        """

        if airport_pos := \
                next(filter(lambda x: x.id == airport_id, airports)):
            airports.remove(airport_pos)
            return True

        return False

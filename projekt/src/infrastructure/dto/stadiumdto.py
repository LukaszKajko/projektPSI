"""A module containing DTO models for output airports."""


from typing import Optional
from asyncpg import Record  # type: ignore
from pydantic import UUID4, BaseModel, ConfigDict

from src.infrastructure.dto.clubdto import ClubDTO


class StadiumDTO(BaseModel):
    """A model representing DTO for airport data."""
    id: int
    name: str
    club: ClubDTO
    user_id: UUID4

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )

    @classmethod
    def from_record(cls, record: Record) -> "StadiumDTO":
        """A method for preparing DTO instance based on DB record.

        Args:
            record (Record): The DB record.

        Returns:
            AirportDTO: The final DTO instance.
        """
        record_dict = dict(record)

        return cls(
            id=record_dict.get("id"),  # type: ignore
            name=record_dict.get("name"),  # type: ignore
            club=ClubDTO(
                id=record_dict.get("id_1"),
                name=record_dict.get("name_1"),
            ),
            user_id=record_dict.get("user_id"),
        )
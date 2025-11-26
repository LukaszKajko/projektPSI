from pydantic import BaseModel, ConfigDict  # type: ignore



class ClubDTO(BaseModel):
    """A model representing DTO for club data."""
    name: str
    place: int
    clubId: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        arbitrary_types_allowed=True,
    )
from pydantic import BaseModel, ConfigDict


class ClubIn(BaseModel):
    name: str
    place: int
    clubId: int


class Club(ClubIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")
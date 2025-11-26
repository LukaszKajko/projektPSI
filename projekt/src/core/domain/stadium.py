from typing import Optional
from fastapi import fastAPI, Depends
from pydantic import BaseModel, ConfigDict


class StadiumIn(BaseModel):
    '''Atrybuty stadionu'''
    clubName: str
    stadiumsName: str
    stadiumsId: int
    amountOfSeats: int


class Stadium(StadiumIn):
    id: int
    model_config = ConfigDict(from_attributes=True, extra="ignore")

app = fastAPI()
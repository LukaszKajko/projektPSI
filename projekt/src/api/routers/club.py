"""A module containing club endpoints."""

from typing import Iterable

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.club import Club, ClubIn
from src.infrastructure.services.iclub import IClubService

router = APIRouter()


@router.post("/create", response_model=Club, status_code=201)
@inject
async def create_club(
    club: ClubIn,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> dict:
    """An endpoint for adding new clubs.

    Args:
        club (ClubIn): The club data.
        service (IClubService, optional): The injected service dependency.

    Returns:
        dict: The new club attributes.
    """

    new_club = await service.add_club(club)

    return new_club.model_dump() if new_club else {}


@router.get("/all", response_model=Iterable[Club], status_code=200)
@inject
async def get_all_clubs(
    service: IClubService = Depends(Provide[Container.club_service]),
) -> Iterable:
    """An endpoint for getting all clubs.

    Args:
        service (IClubService, optional): The injected service dependency.

    Returns:
        Iterable: The club attributes collection.
    """

    clubs = await service.get_all_clubs()

    return clubs


@router.get("/{clubId}", response_model=Club, status_code=200)
@inject
async def get_club_by_id(
    clubId: int,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> dict:
    """An endpoint for getting club details by id.

    Args:
        clubIdd (int): The id of the club.
        service (IClubService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if club does not exist.

    Returns:
        dict: The requested club attributes.
    """

    if club := await service.get_club_by_id(clubId=clubId):
        return club.model_dump()

    raise HTTPException(status_code=404, detail="Club not found")


@router.get(
        "/club/{clubId}",
        response_model=list[Club],
        status_code=200,
)


@router.put("/{clubId}", response_model=Club, status_code=201)
@inject
async def update_club(
    clubId: int,
    updated_club: ClubIn,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> dict:
    """An endpoint for updating club data.

    Args:
        clubId (int): The id of the club.
        updated_club (ClubIn): The updated club details.
        service (IClubService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if club does not exist.

    Returns:
        dict: The updated club data.
    """

    if await service.get_club_by_id(clubId=clubId):
        new_updated_club = await service.update_club(
            clubId=clubId,
            data=updated_club,
        )
        return new_updated_club.model_dump() if new_updated_club else {}

    raise HTTPException(status_code=404, detail="Club not found")


@router.delete("/{clubId}", status_code=204)
@inject
async def delete_club(
    clubId: int,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> None:
    """An endpoint for deleting clubs.

    Args:
        clubId (int): The id of the club.
        service (IClubService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if club does not exist.
    """

    if await service.get_club_by_id(clubId=clubId):
        await service.delete_club(clubId)

        return

    raise HTTPException(status_code=404, detail="Club not found")
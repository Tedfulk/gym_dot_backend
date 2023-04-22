from uuid import UUID

from pydantic import BaseModel


class FacilityUpdates(BaseModel):
    """Fields on the Facility Model that should be updatable."""

    name: str
    address: str | None
    city: str | None
    state: str | None


class NewFacility(FacilityUpdates):
    """Model for creating a new facility, extending FacilityUpdates with attributes that should be unchangable."""


class Facility(NewFacility):
    """Facility with 'id' field"""

    id: UUID


class DeleteFacilityResult(BaseModel):
    """Deleted Facility with 'id' field"""

    id: UUID

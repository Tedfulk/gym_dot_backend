from uuid import UUID

from pydantic import BaseModel

from gym_dot_lib.context.facilities import Facility


class CompanyUpdates(BaseModel):
    """Fields on the Company Model that should be updatable."""

    name: str


class NewCompany(CompanyUpdates):
    """Model for creating a new company, extending CompanyUpdates with attributes that should be unchangable."""


class Company(NewCompany):
    """Company with 'id' field"""

    id: UUID


class CompanyWithFacilities(BaseModel):
    """Company with 'id' field and 'facility' field"""

    id: UUID
    name: str
    facility: list[Facility]


class DeleteCompanyResult(BaseModel):
    """Deleted Company with 'id' field"""

    id: UUID

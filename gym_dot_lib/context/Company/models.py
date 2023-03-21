from pydantic import BaseModel, constr


class CompanyUpdates(BaseModel):
    """Fields on the Company that should be updateable."""

    name: constr(min_length=1, strip_whitespace=True)


class NewCompany(CompanyUpdates):
    """Model for creating a new Company, extending CompanyUpdates with attributes that are not updateable."""

    pass


class Company(NewCompany):
    """Company entity with an id."""

    id: str

from pydantic import BaseModel, constr


class Location(BaseModel):
    """Location entity."""

    address: constr(min_length=3, strip_whitespace=True)
    city: constr(min_length=3, strip_whitespace=True)
    state: constr(min_length=3, strip_whitespace=True)
    country: constr(min_length=3, strip_whitespace=True)


class FacilityUpdates(BaseModel):
    """Fields on the Facility that should be updateable."""

    name: constr(min_length=3, strip_whitespace=True)
    location: Location


class NewFacility(FacilityUpdates):
    """Model for creating a new Facility, extending FacilityUpdates with attributes that are not updateable."""

    pass


class Facility(NewFacility):
    """Facility entity with an id."""

    id: str

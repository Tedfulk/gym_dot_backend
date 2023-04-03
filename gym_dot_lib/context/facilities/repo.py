from .models import FacilityUpdates, NewFacility
from gym_dot_lib.context import client
import pydantic


class FacilityRepo:
    """Methods for Facility entity interacting with edgedb."""

    @pydantic.validate_arguments
    def create(company_id: str, new_facility: NewFacility):
        """Create a new Facility.
        Example:
            FacilityRepo.create(new_facility=NewFacility(**{'name':'junipers company'}))
            FacilityRepo.create(new_facility={"name":"juni compnay"})
        """
        return client.query(
            """
            insert company::Facility {
                name := <str>$name,
            }
        """,
            name=new_facility.name,
        )

    def get(id: str):
        """Get a Facility by id.
        Example:
            FacilityRepo.get(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb')
        """
        return client.query_single(
            """
            select facility::Facility {
                id,
                name,
            }
            filter .id = <uuid>$id
        """,
            id=id,
        )

    @pydantic.validate_arguments
    def update(id: str, updates: FacilityUpdates):
        """Update a Facility by id.
        Example:
            FacilityRepo.update(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb', updates=FacilityUpdates(**{'name':'junipers company'}))
        """
        return client.query(
            """
            update facility::Facility
            filter .id = <uuid>$id
            set {
                name := <str>$name,
            }
        """,
            id=id,
            name=updates.name,
        )

    def delete(id: str):
        """Delete a Facility by id.
        Example:
            FacilityRepo.delete(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb')
        """
        return client.query(
            """
            delete
            filter .id = <uuid>$id
        """,
            id=id,
        )

    def get_all():
        """Get all Facilities.
        Example:
            FacilityRepo.get_all()
        """
        return client.query(
            """
            select facility::Facility {
                id,
                name,
            }
        """
        )

    def get_all_by_company_id(company_id: str):
        """Get all Facilities by company_id.
        Example:
            FacilityRepo.get_all_by_company_id(company_id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb')
        """
        return client.query(
            """
            select facility::Facility {
                id
                name
            }
            filter .company_id = <uuid>$company_id
        """,
            company_id=company_id,
        )

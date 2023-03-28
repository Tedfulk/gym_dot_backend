from .models import CompanyUpdates, NewCompany
from gym_dot_lib.context import client
import pydantic


class CompanyRepo:
    """Methods for Company entity interacting with edgedb."""

    @pydantic.validate_arguments
    def create(new_company: NewCompany):
        """Create a new Company.
        Example:
            CompanyRepo.create(new_company=NewCompany(**{'name':'junipers company'}))
            CompanyRepo.create(new_company={"name":"juni compnay"})
        """
        return client.query(
            """
            insert company::Company {
                name := <str>$name,
            }
        """,
            name=new_company.name,
        )

    def get(id: str):
        """Get a Company by id.
        Example:
            CompanyRepo.get(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb')
        """
        return client.query(
            """
            select company::Company {
                id,
                name,
            }
            filter .id = <uuid>$id
        """,
            id=id,
        )

    @pydantic.validate_arguments
    def update(id: str, updates: CompanyUpdates):
        """Update a Company by id.
        Example:
            CompanyRepo.update(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb', updates=CompanyUpdates(**{'name':'junipers company'}))
        """
        return client.query(
            """
            update company::Company
            filter .id = <uuid>$id
            set {
                name := <str>$name,
            }
        """,
            id=id,
            name=updates.name,
        )

    def delete(id: str):
        """Delete a Company by id.
        Example:
            CompanyRepo.delete(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb')
        """
        return client.query(
            """
            delete company::Company
            filter .id = <uuid>$id
        """,
            id=id,
        )

    def all_companies():
        """List all Companies.
        Example:
            CompanyRepo.all_companies()
        """
        return client.query(
            """
            select company::Company {
                id,
                name,
                facility: {
                    id,
                    address,
                    city,
                    name,
                    state
            }
        }
        """
        )

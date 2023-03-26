from .models import CompanyUpdates, NewCompany, Company
import pydantic
import edgedb

client = edgedb.create_client()


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
            INSERT company::Company {
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
        return client.query_single(
            """
            SELECT company::Company {
                id,
                name,
            }
            FILTER .id = <uuid>$id
        """,
            id=id,
        )

    def update(id: str, updates: CompanyUpdates):
        """Update a Company by id.
        Example:
            CompanyRepo.update(id='1bd1374c-ca62-11ed-acf2-4fed2a055fdb', updates=CompanyUpdates(**{'name':'junipers company'}))
        """
        return client.query(
            """
            UPDATE company::Company
            FILTER .id = <uuid>$id
            SET {
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
            DELETE company::Company
            FILTER .id = <uuid>$id
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
            SELECT company::Company {
                id,
                name,
            }
        """
        )

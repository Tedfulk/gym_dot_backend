from .models import CompanyUpdates, NewCompany, Company
import edgedb

client = edgedb.create_client()


class CompanyRepo:
    """Methods for Company entity interacting with edgedb."""

    def create(new_company: NewCompany):
        """Create a new Company."""
        return client.query(
            """
            INSERT Company {
                name := <str>$name,
            }
        """,
            name=new_company.name,
        )

    def get(id: str):
        """Get a Company by id."""
        return client.query_single(
            """
            SELECT Company {
                id,
                name,
            }
            FILTER .id = <uuid>$id
        """,
            id=id,
        )

    def update(id: str, company: CompanyUpdates):
        """Update a Company by id."""
        pass

    def delete(id: str):
        """Delete a Company by id."""
        return client.query(
            """
            DELETE Company
            FILTER .id = <uuid>$id
        """,
            id=id,
        )

    def list():
        """List all Companies."""
        return client.query(
            """
            SELECT Company {
                id,
                name,
            }
        """
        )

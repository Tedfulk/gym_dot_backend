import pytest

from api.gym_dot_lib.context.companies import (
    AllCompaniesResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetCompanyResult,
    UpdateCompanyResult,
)
from api.gym_dot_lib.context.main import client

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio

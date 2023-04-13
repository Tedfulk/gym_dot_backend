import pytest

from api.gym_dot_lib.context.companies import (
    AllCompaniesResult,
    CreateCompanyResult,
    DeleteCompanyResult,
    GetCompanyResult,
    UpdateCompanyResult,
    all_companies,
    create_company,
    delete_company,
    get_company,
    update_company,
)
from api.gym_dot_lib.context.main import client

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

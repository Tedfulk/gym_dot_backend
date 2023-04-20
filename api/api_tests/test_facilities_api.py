import pytest

from api.gym_dot_lib.context.facilities import (
    CreateFacilityResult,
    create_facility,
    delete_facility,
    DeleteFacilityResult,
    AllFacilitiesResult,
    UpdateFacilityResult,
    update_facility,
    all_facilities,
    get_facility,
    GetFacilityResult,
)
from api.main import async_client as AC

# NOTE: 'import *' makes sure all the needed fixtures are in scope for these tests.
from api.sample_data import *

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio

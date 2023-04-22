ALL_FACILITIES = r"""
select Facilities {
    id,
    name,
    address,
    city,
    state,
}
"""


CREATE_FACILITY = r"""
select (
    insert Facilities {
        name := <str>$name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
) {
    id,
    name,
    address,
    city,
    state
}
"""

DELETE_FACILITY = r"""
delete Facilities
    filter .id = <uuid>$facility_id
"""

GET_FACILITY = r"""
select Facilities {
    id,
    name,
    address,
    city,
    state,
    }
    filter .id = <uuid>$facility_id
"""

UPDATE_FACILITY = r"""
select (
    update Facilities
    filter .id = <uuid>$facility_id
    set {
        name := <str>$name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
) {
    id,
    name,
    address,
    city,
    state,
}
"""

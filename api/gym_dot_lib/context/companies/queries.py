GET_COMPANY = r"""
select Companies {
        id,
        name,
    }
    filter .id = <uuid>$company_id
"""

ADD_FACILITY = r"""
select(
    update Companies
        filter .id=<uuid>$company_id
        set {
            facility += (select detached Facilities
                filter .id=<uuid>$facility_id )
    }
) {
    id,
    name,
}
"""

ALL_COMPANIES = r"""
select Companies {
        id,
        name,
}
"""

CREATE_COMPANY_AND_FACILTY = r"""
select (
insert Companies {
    name := <str>$company_name,
    facility := {
    (insert Facilities {
        name := <str>$facility_name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
    )
    }
}
) {
    id,
    name,
    facility: {
    id,
    name,
    address,
    city,
    state
    }
}
"""

CREATE_COMPANY = r"""
select (
    insert Companies {
        name := <str>$company_name,
    }
) {
    id,
    name
}
"""

DELETE_COMPANY = r"""
delete Companies
    filter .id = <uuid>$company_id
"""

GET_FACILITIES = r"""
select Companies {
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
filter .id=<uuid>$company_id
"""

REMOVE_FACILITY = r"""
select(
    update Companies
    filter .id=<uuid>$company_id
    set {
        facility -= (select detached Facilities
        filter .id=<uuid>$facility_id )
    }
) {
    id,
    name,
}
"""

UPDATE_COMPANY = r"""
select (
    update Companies
        filter .id = <uuid>$company_id
        set {
            name := <str>$company_name,
        }
) {
    id,
    name,
}
"""

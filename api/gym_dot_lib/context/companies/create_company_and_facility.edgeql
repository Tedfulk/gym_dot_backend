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

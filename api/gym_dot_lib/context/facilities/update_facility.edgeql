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
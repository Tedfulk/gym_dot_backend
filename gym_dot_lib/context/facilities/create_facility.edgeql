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

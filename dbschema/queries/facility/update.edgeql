update company::Facilities
    filter .id = <uuid>$id
    set {
        name := <str>$name,
        address := <str>$address,
        city := <str>$city,
        state := <str>$state,
    }
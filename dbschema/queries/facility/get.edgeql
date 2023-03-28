select company::Facilities {
    id,
    name,
    address,
    city,
    state,
    }
    filter .id = <uuid>$id
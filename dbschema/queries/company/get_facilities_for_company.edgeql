select company::Company {
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
filter .id=<uuid>$id
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
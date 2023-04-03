update Companies
    filter .id = <uuid>$company_id
    set {
        name := <str>$company_name,
    }
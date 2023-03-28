select company::Company {
                id,
                name,
            }
            filter .id = <uuid>$id
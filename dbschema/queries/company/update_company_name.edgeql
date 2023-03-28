update company::Company
    filter .id = <uuid>$id
    set {
        name := <str>$name,
    }
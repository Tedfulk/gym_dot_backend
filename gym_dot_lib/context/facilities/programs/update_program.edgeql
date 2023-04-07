select (
    update Programs
    filter .id = <uuid>$id
    set {
        name := <str>$name,
        description := <str>$description,
        active := <bool>$active,
    }
) {
    id,
    name,
    description,
    active,
}
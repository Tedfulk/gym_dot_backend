select Programs {
    id,
    name,
    description,
    active,
} filter .id = <uuid>$program_id
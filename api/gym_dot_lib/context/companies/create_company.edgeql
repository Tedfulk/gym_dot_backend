select (
    insert Companies {
        name := <str>$company_name,
    }
) {
    id,
    name
}
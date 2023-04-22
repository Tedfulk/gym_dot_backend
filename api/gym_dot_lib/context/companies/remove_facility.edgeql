select(
  update Companies
  filter .id=<uuid>$company_id
  set {
    facility -= (select detached Facilities
      filter .id=<uuid>$facility_id )
  }
) {
    id,
    name,
}

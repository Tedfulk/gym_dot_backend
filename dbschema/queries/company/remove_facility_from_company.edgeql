update company::Company 
  filter .id=<uuid>$company_id
  set {
    facility -= (select detached company::Facilities 
                 filter .id=<uuid>$facility_id )
  }
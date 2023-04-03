select (
  insert Companies {
    name := <str>$comapny_name,
    facility := (
      insert Facilities {
          name := <str>$facility_name, 
          address := <str>$address,
          city := <str>$city,
          state := <str>$state,
        }
      )
    } 
  ){
      name,
      facility: {
        name,
        address,
        city,
        state
      }
    }